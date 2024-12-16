from pretext.project import Project
from git import Repo
from pathlib import Path

p = Project()
repo = Repo()
commit_head = repo.commit("HEAD")
commit_origin_main = repo.commit("main")
commit_merge_base = repo.merge_base(commit_head, commit_origin_main)
diff_index = commit_origin_main.diff(commit_merge_base)
changed_files = [Path(item.a_path) for item in diff_index]
