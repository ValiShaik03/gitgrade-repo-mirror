import requests

def analyze_repo(repo_url):
    parts = repo_url.rstrip("/").split("/")
    owner, repo = parts[-2], parts[-1]

    base_api = f"https://api.github.com/repos/{owner}/{repo}"

    repo_res = requests.get(base_api).json()
    if "message" in repo_res:
        raise Exception("Repository not found")

    commits_res = requests.get(base_api + "/commits").json()
    contents_res = requests.get(base_api + "/contents").json()

    readme_exists = False
    if isinstance(contents_res, list):
        readme_exists = any(
            item.get("name", "").lower().startswith("readme")
            for item in contents_res
        )

    return {
        "stars": repo_res.get("stargazers_count", 0),
        "language": repo_res.get("language"),
        "commits": len(commits_res) if isinstance(commits_res, list) else 0,
        "files": len(contents_res) if isinstance(contents_res, list) else 0,
        "readme": readme_exists
    }
