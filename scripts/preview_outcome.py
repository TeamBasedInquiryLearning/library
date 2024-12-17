import argparse
import shutil
from pathlib import Path
import os
import subprocess
import zipfile
import lxml.etree as ET
from checkit.bank import Bank
from checkit import static

def build_preview(book:str, outcome:str, amount:int = 20):
    # check that this outcome exists
    exercise_path = Path("source", book, "exercises")
    sage_library_path = Path("source", book, "sage")
    bank_root = ET.parse(exercise_path/"bank.xml")
    search_string = f'.//*[name()="slug" and text()="{outcome}"]/./..'
    try:
        outcome_ele = bank_root.xpath(search_string)[0]
    except IndexError:
        error_message = f"{outcome} is not an outcome defined in {exercise_path}/bank.xml"
        raise ValueError(error_message)

    # get path to sandbox
    sandbox_path = Path("exercise-sandbox")
    sandbox_bank_path = sandbox_path/"bank"

    # destroy any existing sandbox
    shutil.rmtree(sandbox_path, ignore_errors=True)

    # create new sandbox with that outcome
    sandbox_path.mkdir()
    sandbox_bank_path.mkdir()
    (sandbox_bank_path/"bank.xml").write_text(f"""
    <?xml version='1.0' encoding='UTF-8'?>
    <bank xmlns="https://checkit.clontz.org" version="0.2">
        <title>Preview: {book} {outcome}</title>
        <slug>preview</slug>
        <url>https://tbil.org</url>
        <outcomes>
            <outcome>
                <title>{outcome_ele.find("{*}title").text}</title>
                <slug>{outcome}</slug>
                <path>outcome</path>
                <description>{outcome_ele.find("{*}description").text}</description>
            </outcome>
        </outcomes>
    </bank>
    """.strip())
    (sandbox_bank_path/"outcome").mkdir(exist_ok=True)
    (sandbox_path/"sage").mkdir()
    if book in ["linear-algebra", "precalculus"]:
        shutil.copy(sage_library_path/"common.sage", sandbox_path/"sage"/"common.sage")
    outcome_path = (exercise_path/outcome_ele.find("{*}path").text)
    shutil.copy(outcome_path/"template.xml", sandbox_bank_path/"outcome"/"template.xml")
    shutil.copy(outcome_path/"generator.sage", sandbox_bank_path/"outcome"/"generator.sage")


    # quick and dirty validation
    template_root = ET.parse(sandbox_bank_path/"outcome"/"template.xml")
    valid_tags = ["knowl", "title", "intro", "content", "outtro", "p", "list", "item", "m", "me",
                "q", "c", "em", "url", "image"]
    for b in template_root.xpath('//*'):
        bare_tag = b.tag.split("}")[1].lower()  # remove "${https://spatext.clontz.org}" namespace
        if bare_tag not in valid_tags:
            raise Exception(f"Template includes an invalid SpaTeXt tag: ${b.tag}")


    b = Bank(str(sandbox_path/"bank"))
    print(f"Generating {amount} exercises")

    # build {amount} seeds and images
    cmds = [
        "sage",
        os.path.join("scripts", "_preview_outcome.sage"),
        outcome, 
        f"{amount}"
    ]
    subprocess.run(cmds,check=True)

    b.write_json()

    # b.build_viewer() # <-- broken, reimplemented below
    docs_path = os.path.join(b.abspath(), "docs")
    if os.path.exists(docs_path) and os.path.isdir(docs_path):
        shutil.rmtree(docs_path)
    os.makedirs(docs_path)
    archive = zipfile.ZipFile(static.open_resource("viewer.zip"))
    archive.extractall(docs_path)
    # copy assets
    shutil.copytree(b.build_path(), os.path.join(docs_path, "assets"), dirs_exist_ok=True)

    return sandbox_bank_path


def main(book:str, outcome:str, amount:int = 20):
    sandbox_bank_path = build_preview(book, outcome, amount)

    subprocess.run(['python', '-m', 'http.server', '-d', str(sandbox_bank_path/'docs')])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Preview a CheckIt outcome.')
    parser.add_argument('book', choices=['precalculus', 'calculus', 'linear-algebra'])
    parser.add_argument('outcome')
    parser.add_argument('--all', action=argparse.BooleanOptionalAction)
    args = parser.parse_args()
    if args.all:
        amount = 1000
    else:
        amount = 20
    main(book=args.book, outcome=args.outcome, amount=amount)
