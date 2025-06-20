# backend/utils/git_ops.py

import os
import subprocess

def clone_or_pull_repo(repo_url: str, clone_path: str = "./repos") -> str:
    os.makedirs(clone_path, exist_ok=True)
    repo_name = repo_url.split("/")[-1].replace(".git", "")
    repo_path = os.path.join(clone_path, repo_name)

    if os.path.exists(repo_path):
        subprocess.run(["git", "-C", repo_path, "pull"])
    else:
        subprocess.run(["git", "clone", repo_url, repo_path])

    return repo_path

def get_repo_diff(repo_path: str, file_path: str = "") -> str:
    args = ["git", "-C", repo_path, "diff", "HEAD~1", "HEAD"]
    if file_path:
        args.append(file_path)

    result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.decode("utf-8")
