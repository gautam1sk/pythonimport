from git import Repo

repo_dir = 'C:/Users/gannam/Documents/pythonimport'
repo = Repo(repo_dir)
file_list = [
    'hellopython.txt'
]
commit_message = 'Add simple regression analysis'
repo.index.add(repo.untracked_files)
repo.index.commit("python first import 2")
origin = repo.remote('origin')
origin.push()
