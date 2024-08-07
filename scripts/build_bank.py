import argparse
from pathlib import Path
import shutil
import zipfile
from checkit.bank import Bank
from checkit import static

def main(book:str, full:bool, sandbox=False, stage=True):

    if sandbox:
        base_path = Path("edition-sandbox")
    else:
        base_path = Path(".")
    bank_path = base_path / "source" / book / "exercises"

    print(f"Building exercises from `{bank_path}`")

    b = Bank(bank_path)
    b.generate_exercises(regenerate=full, images=full)
    b.write_json()

    # b.build_viewer() # <-- broken, reimplemented below
    docs_path = Path(b.abspath()) / "docs"
    if docs_path.exists() and docs_path.is_dir():
        shutil.rmtree(docs_path)
    docs_path.mkdir()
    archive = zipfile.ZipFile(static.open_resource("viewer.zip"))
    archive.extractall(docs_path)
    # copy assets
    shutil.copytree(b.build_path(), docs_path / "assets", dirs_exist_ok=True)

    if stage:
        stage_path = base_path / "output" / "stage" / "preview" / book / "exercises"
        print(f"Staging bank at `{stage_path}`")
        # stage bank
        shutil.copytree(
            docs_path, 
            stage_path, 
            dirs_exist_ok=True
        )

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Build a CheckIt bank.')
    parser.add_argument('book', choices=['precalculus', 'calculus', 'linear-algebra'])
    parser.add_argument('-f', '--full',
                        action='store_true')
    args = parser.parse_args()
    main(book=args.book, full=args.full)
