import argparse
import glob
from pathlib import Path
import shutil
import subprocess
from pretext.project import Project
from pretext import logger
from . import build_bank
import logging

log = logging.getLogger("ptxlogger")
logger.add_log_stream_handler()
log.setLevel(logging.DEBUG)

def build_books(stage_directory=None, books=None):
    if books is None:
        books = ["calculus", "linear-algebra", "precalculus"]
    p = Project.parse()
    for book in books:
        p.get_target(f"{book}-web").build(clean=True)
        p.get_target(f"{book}-web-instructor").build(clean=True)
        p.get_target(f"{book}-print").build(clean=True)
        p.get_target(f"{book}-print-instructor").build(clean=True)
        p.get_target(f"{book}-print-slides").build(clean=True)
        if stage_directory is not None:
            stage_path = Path() / "output" / "stage" / stage_directory / book
            print(f"Staging book at `{stage_path}`")
            # stage book
            shutil.copytree(
                Path("output") / f"{book}-web", 
                stage_path, 
                dirs_exist_ok=True
            )
            shutil.copytree(
                Path("output") / f"{book}-web-instructor", 
                stage_path / "instructor", 
                dirs_exist_ok=True
            )
            shutil.copytree(
                Path("output") / f"{book}-print", 
                stage_path / "print", 
                dirs_exist_ok=True
            )
            shutil.copytree(
                Path("output") / f"{book}-print-slides", 
                stage_path / "print", 
                dirs_exist_ok=True
            )
            shutil.copytree(
                Path("output") / f"{book}-print-instructor", 
                stage_path / "print", 
                dirs_exist_ok=True
            )

def build_banks(stage_directory=None, books=None):
    if books is None:
        books = ["calculus", "linear-algebra", "precalculus"]
    # build and stage banks
    for book in books:
        build_bank.main(book=book, full=True, stage_directory=stage_directory)

def main(stage_directory=None):
    build_books(stage_directory=stage_directory)
    build_banks(stage_directory=stage_directory)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Build fixed editions of books.')
    parser.add_argument('stage_directory')
    args = parser.parse_args()
    main(stage_directory=args.stage_directory)
