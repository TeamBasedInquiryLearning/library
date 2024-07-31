import argparse
import os
import shutil
import zipfile
from checkit.bank import Bank
from checkit import static

parser = argparse.ArgumentParser(description='Build a CheckIt bank.')
parser.add_argument('book', choices=['precalculus', 'calculus', 'linear-algebra'])
parser.add_argument('-f', '--full',
                    action='store_true')
args = parser.parse_args()

bank_path = os.path.join("source", args.book, "exercises")

print(f"Building exercises from `{bank_path}`")

b = Bank(bank_path)
b.generate_exercises(regenerate=args.full, images=args.full)
b.write_json()

# b.build_viewer() # <-- broken, reimplemented below
docs_path = os.path.join(b.abspath(), "docs")
if os.path.exists(docs_path) and os.path.isdir(docs_path):
    shutil.rmtree(docs_path)
os.makedirs(docs_path)
archive = zipfile.ZipFile(static.open_resource("viewer.zip"))
archive.extractall(docs_path)
# copy assets
shutil.copytree(b.build_path(), os.path.join(docs_path,"assets"), dirs_exist_ok=True)

stage_path = os.path.join("output", "stage", args.book, "preview", "exercises")
print(f"Staging bank at `{stage_path}`")
# stage bank
shutil.copytree(
    docs_path, 
    stage_path, 
    dirs_exist_ok=True
)
