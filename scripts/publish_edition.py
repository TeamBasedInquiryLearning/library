import argparse
import glob
from pathlib import Path
import shutil
import subprocess
import build_bank
from pretext.project import Project

def main(name:str, slug:str):
 
    # update edition name
    files = glob.glob('source/**/source/main.ptx')
    files += glob.glob('source/**/exercises/bank.xml')
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
    files = glob.glob('source/**/source/**/*.ptx')
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

    # # build and stage targets
    p = Project.parse()
    for t in p.deploy_targets():
        t.build(clean=True)
    p.stage_deployment()

    # build and stage banks
    for book in ["precalculus", "calculus", "linear-algebra"]:
        build_bank.main(book=book, full=True)

    # undo changes to source
    subprocess.run("git", "reset", "HEAD", "--hard")

    # save edition to site directory
    shutil.copytree(
        Path("output", "stage", "calculus", "preview"),
        Path("site", "calculus", slug)
    )
    shutil.copytree(
        Path("output", "stage", "precalculus", "preview"),
        Path("site", "precalculus", slug)
    )
    shutil.copytree(
        Path("output", "stage", "linear-algebra", "preview"),
        Path("site", "linear-algebra", slug)
    )

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Build fixed editions of books.')
    parser.add_argument('edition_name')
    parser.add_argument('edition_slug')
    args = parser.parse_args()
    main(name=args.edition_name, slug=args.edition_slug)
