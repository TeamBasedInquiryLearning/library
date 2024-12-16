from pretext.project import Project
from git import Repo
from gitdb import GitDB
from pathlib import Path
from lxml import etree

repo = Repo(odbt=GitDB) # https://github.com/gitpython-developers/GitPython/discussions/1180#discussioncomment-408868
repo.config("--global", "--add", "safe.directory", Path("."))
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
        
