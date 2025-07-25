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

def build_books(books=None):
    if books is None:
        books = ["calculus", "linear-algebra", "precalculus"]
    p = Project.parse()
    for book in books:
        p.get_target(f"{book}-web").build(clean=True)
        p.get_target(f"{book}-web-instructor").build(clean=True)
        p.get_target(f"{book}-print").build(clean=True)
        p.get_target(f"{book}-print-instructor").build(clean=True)
        p.get_target(f"{book}-print-slides").build(clean=True)

def build_banks(books=None):
    if books is None:
        books = ["calculus", "linear-algebra", "precalculus"]
    # build and stage banks
    for book in books:
        build_bank.main(book=book, full=True)

def main():
    build_books()
    build_banks()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Build fixed editions of books.')
    args = parser.parse_args()
    main()
