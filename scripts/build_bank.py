import argparse
from pathlib import Path
import shutil
import zipfile
from checkit.bank import Bank
from checkit import static

def main(book:str, full:bool, stage_preview=True):

    bank_path = Path() / "source" / book / "exercises"

    print(f"Building exercises from `{bank_path}`")

    b = Bank(bank_path)
    for o in b.outcomes():
        o.download_cache(f"https://tbil.org/preview/{book}/exercises")
    b.generate_exercises(regenerate=full, images=full)
    b.write_json()

    b.build_viewer(with_cache=True)

    if stage_preview:
        stage_path = Path() / "output" / "stage" / "preview" / book / "exercises"
        print(f"Staging bank at `{stage_path}`")
        # stage bank
        shutil.copytree(
            bank_path / "docs", 
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
