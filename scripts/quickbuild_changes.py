from pretext.project import Project
from git import Repo
from pathlib import Path
from lxml import etree

repo = Repo()
commit_head = repo.commit("HEAD")
commit_origin_main = repo.commit("main")
commit_merge_base = repo.merge_base(commit_head, commit_origin_main)[0]
diff_index = commit_merge_base.diff(commit_head)
changed_files = [Path(item.a_path) for item in diff_index]

p = Project()
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
        root = etree.parse(f)
        xml_id = root.get(r"{http://www.w3.org/XML/1998/namespace}id")
        t.build(xmlid=xml_id, no_knowls=True)
        
