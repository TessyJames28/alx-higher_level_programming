#!/usr/bin/python3
"""
Python script that takes 2 arguments to print the last 10 commits of the repo
    The first argument will be the repository name
    The second argument will be the owner name
    You must use the packages requests and sys
"""
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    r = requests.get(url)
    commits = r.json()
    count = 0
    for commit in commits[:10]:
        sha = commit["sha"]
        author = commit["commit"]["author"]["name"]
        print(f"{sha}: {author}")
        count += 1
