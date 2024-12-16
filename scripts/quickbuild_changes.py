from pretext.project import Project
from git import Repo
from pathlib import Path

p = Project()
repo = Repo()
commit_head = repo.commit("HEAD")
commit_origin_main = repo.commit("main")
commit_merge_base = repo.merge_base(commit_head, commit_origin_main)[0]
diff_index = commit_merge_base.diff(commit_head)
changed_files = [Path(item.a_path) for item in diff_index]
