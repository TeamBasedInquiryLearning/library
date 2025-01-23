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
    changed_files = [Path(item.a_path) for item in diff_index if not item.deleted_file and not item.renamed_file]
    preview_links = []

    p = Project.parse()
    BOOKS = ['precalculus', 'calculus', 'linear-algebra']

    # for each .ptx file, try to build subtree of document
    for b in BOOKS:
        # collect changed xml_ids
        xml_ids = []
        for f in changed_files:
            if Path("source", b) in f.parents and f.suffix == ".ptx":
                root = etree.parse(f).getroot()
                if root.tag in ["section", "chapter", "preface", "appendix", "frontmatter"]:
                    xml_id = root.get(r"{http://www.w3.org/XML/1998/namespace}id")
                    xml_ids.append({
                        "file": f,
                        "id": xml_id,
                    })
        t = p.get_target(f"{b}-web-instructor")
        if len(xml_ids) > 0:
            print(f"Building book `{b}`, skipping images")
            path = f"/preview/{b}/instructor"
            t.build(xmlid=None, no_knowls=True, generate=False)
            preview_links.append({
                "file": b,
                "path": path
            })
        built_ids = set()
        for xml_id in xml_ids:
            if xml_id["id"] not in built_ids:
                print(f"Building book `{b}` with ID `{xml_id["id"]}`")
                t.build(xmlid=xml_id["id"], no_knowls=True, generate=True)
                built_ids.add(xml_id["id"])
            preview_links.append({
                "file": xml_id["file"],
                "path": f"/preview/{b}/instructor/{xml_id["id"]}.html"
            })
    # for each CheckIt file, build its preview
    for b in BOOKS:
        # collect changed outcomes
        changed_outcomes = set()
        for f in changed_files:
            if Path("source", b, "exercises", "outcomes") in f.parents:
                changed_outcomes.add(f.parent.name)
        # build changed outcomes
        for o in changed_outcomes:
            sandbox_bank_path = preview_outcome.build_preview(b, o)
            output_path = Path("output", f"{b}-web-instructor", "exercises", o)
            output_path.mkdir(parents=True)
            shutil.copytree(sandbox_bank_path / "docs", output_path, dirs_exist_ok=True)
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

