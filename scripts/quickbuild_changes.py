from pretext.project import Project
from git import Repo
from pathlib import Path
from lxml import etree
import os
import shutil
from . import preview_outcome

def main():
    repo = Repo()
    commit_head = repo.commit("HEAD")
    commit_origin_main = repo.commit("origin/main")
    commit_merge_base = repo.merge_base(commit_head, commit_origin_main)[0]
    diff_index = commit_merge_base.diff(commit_head)
    changed_files = [Path(item.a_path) for item in diff_index]
    preview_links = []

    p = Project.parse()
    BOOKS = ['precalculus', 'calculus', 'linear-algebra']

    # for each .ptx file, try to build subtree of document
    for f in [f for f in changed_files if f.suffix == ".ptx"]:
        book = None
        for b in BOOKS:
            b_path = Path("source") / b
            if b_path in f.parents:
                book = b
        if book is not None:
            t = p.get_target(f"{book}-web-instructor")
            root = etree.parse(f).getroot()
            xml_id = root.get(r"{http://www.w3.org/XML/1998/namespace}id")
            print(f"Building book `{book}` with ID `{xml_id}`")
            title_ele = root.find("title")
            if title_ele is None:
                if xml_id is None:
                    path = f"/preview/{book}/instructor"
                else:
                    path = f"/preview/{book}/instructor/{xml_id}.html"
            else:
                path = f"/preview/{book}/instructor/{xml_id}.html"
            t.build(xmlid=xml_id, no_knowls=True, generate=(xml_id is not None))
            preview_links.append({
                "file": f,
                "path": path
            })
    # for each CheckIt file, build its preview
    for b in BOOKS:
        EXERCISE_FILES = [f for f in changed_files if Path("source", b, "exercises", "outcomes") in f.parents]
        # collect changed outcomes
        changed_outcomes = []
        for f in EXERCISE_FILES:
            if f.parent.name not in changed_outcomes:
                changed_outcomes.append(f.parent.name)
        # build changed outcomes
        for o in changed_outcomes:
            _, sandbox_bank_path = preview_outcome.build_preview(b, o)
            output_path = Path("output", f"{b}-web-instructor", "exercises", o)
            output_path.mkdir(parents=True)
            shutil.copytree(sandbox_bank_path, output_path, dirs_exist_ok=True)
            preview_links.append({
                "file": f,
                "path": f"/preview/{b}/instructor/exercises/{o}/"
            })


    
    # create Javascript template for markdown output
    markdown = f"## 🚀 Preview available 🚀\n\n<${{cf_url}}>\n\n"
    for link in preview_links:
        # ${{cf_url}} is provided by action Javascript
        markdown += f"- \\`{link["file"]}\\`: <${{cf_url}}{link["path"]}>\n"
    with open(os.environ["GITHUB_OUTPUT"], 'a') as fh:
        fh.write(f"markdown<<MARKDOWN\n{markdown}\nMARKDOWN\n")
        
if __name__ == "__main__":
    main()

