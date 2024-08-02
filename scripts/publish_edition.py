import argparse
import glob
from pathlib import Path
import shutil
import subprocess
from pretext.project import Project
from . import build_bank

def clean_edition_sandbox():
    # delete subdirectory
    subprocess.run(["rm", "-rf", "edition-sandbox"])
    # copy repo to subdirectory
    subprocess.run(["git", "clone", ".", "edition-sandbox"])

def update_edition_source(name:str, slug:str):
    # update edition name
    files = glob.glob('edition-sandbox/source/**/source/main.ptx')
    files += glob.glob('edition-sandbox/source/**/exercises/bank.xml')
    for filestr in files:
        # Read in the file
        with open(filestr, 'r') as file:
            filedata = file.read()
        # Replace the target string
        filedata = filedata.replace(
            "PREVIEW Edition",
            f"{name} Edition"
        )
        # Write the file out again
        with open(filestr, 'w') as file:
            file.write(filedata)

    # update edition links
    files = glob.glob('edition-sandbox/source/**/source/**/*.ptx')
    for filestr in files:
        # Read in the file
        with open(filestr, 'r') as file:
            filedata = file.read()
        # Replace the target string
        filedata = filedata.replace(
            "https://tbil.org/calculus/preview", 
            f"https://tbil.org/calculus/{slug}"
        )
        filedata = filedata.replace(
            "https://tbil.org/precalculus/preview", 
            f"https://tbil.org/precalculus/{slug}"
        )
        filedata = filedata.replace(
            "https://tbil.org/linear-algebra/preview", 
            f"https://tbil.org/linear-algebra/{slug}"
        )
        # Write the file out again
        with open(filestr, 'w') as file:
            file.write(filedata)

def build_books(slug:str, books=None):
    if books is None:
        books = ["calculus", "linear-algebra", "precalculus"]
    # # build and stage targets
    p = Project.parse("edition-sandbox")
    for t in p.deploy_targets():
        t.build(clean=True)
    p.stage_deployment()
    # save edition to site directory
    for book in books:
        shutil.copytree(
            Path("edition-sandbox", "output", "stage", book, "preview"),
            Path("site", book, slug)
        )

def build_banks(slug:str, books=None):
    if books is None:
        books = ["calculus", "linear-algebra", "precalculus"]
    # build and stage banks
    for book in books:
        build_bank.main(book=book, full=True)
        shutil.copytree(
            Path("edition-sandbox", "output", "stage", book, "preview", "exercises"),
            Path("site", book, slug, "exercises")
        )

def main(name:str, slug:str, clean=True):
    if clean:
        clean_edition_sandbox()
    update_edition_source(name, slug)
    build_books(slug)
    build_banks(slug)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Build fixed editions of books.')
    parser.add_argument('edition_name')
    parser.add_argument('edition_slug')
    args = parser.parse_args()
    main(name=args.edition_name, slug=args.edition_slug)
