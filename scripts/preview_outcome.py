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
    sandbox_path = Path("exercise-sandbox")/"subject"
    sandbox_bank_path = sandbox_path/"bank"

    # destroy any existing sandbox
    shutil.rmtree(sandbox_path, ignore_errors=True)
    shutil.copytree(exercise_path, sandbox_bank_path, dirs_exist_ok=True)

    outcome_path = outcome_ele.find("{*}path").text

    # quick and dirty validation
    template_root = ET.parse(sandbox_bank_path/outcome_path/"template.xml")
    valid_tags = ["knowl", "title", "intro", "content", "outtro", "p", "list", "item", "m", "me",
                "q", "c", "em", "url", "image"]
    for b in template_root.xpath('//*'):
        bare_tag = b.tag.split("}")[1].lower()  # remove "${https://spatext.clontz.org}" namespace
        if bare_tag not in valid_tags:
            raise Exception(f"Template includes an invalid SpaTeXt tag: ${b.tag}")


    b = Bank(str(sandbox_bank_path))
    b._outcomes = [o for o in b._outcomes if o.slug.lower() == outcome.lower()]
    b.title = f"Preview of {b.title}: {outcome}"
    b.generate_exercises(regenerate=True,images=True,amount=amount)
    b.write_json()
    b.build_viewer()

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
