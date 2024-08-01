import argparse
import glob
import build_bank
from pretext.project import Project

def main():
    parser = argparse.ArgumentParser(description='Build fixed editions of books.')
    parser.add_argument('edition_name')
    parser.add_argument('edition_slug')
    args = parser.parse_args()
 
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
            f"{args.edition_name} Edition"
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
            f"https://tbil.org/calculus/{args.edition_slug}"
        )
        filedata = filedata.replace(
            "https://tbil.org/precalculus/preview", 
            f"https://tbil.org/precalculus/{args.edition_slug}"
        )
        filedata = filedata.replace(
            "https://tbil.org/linear-algebra/preview", 
            f"https://tbil.org/linear-algebra/{args.edition_slug}"
        )
        # Write the file out again
        with open(filestr, 'w') as file:
            file.write(filedata)

    # p = Project.parse()
    # for t in p.deploy_targets():
    #     t.build()

    # build_bank.main()

if __name__ == "__main__":
    main()
