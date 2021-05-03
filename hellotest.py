from git import Repo

repo_dir = 'C:/Users/gannam/Documents/pythonimport'
repo = Repo(repo_dir)
file_list = [
    'hellopython.txt'
]
count_modified_files = len(repo.index.diff(None))
print(count_modified_files)
if count_modified_files >0:
    commit_message = 'Add simple regression analysis'
    repo.index.add(item.a_path for item in repo.index.diff(None))
    repo.index.commit("python first import 2")
    origin = repo.remote('origin')
    origin.push()
