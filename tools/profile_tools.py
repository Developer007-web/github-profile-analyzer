from services.github_api import GitHubAPI
from services.analyzer import Analyzer

api = GitHubAPI()


async def analyze_profile(username: str):

    profile = await api.get_user(username)
    repos = await api.get_repositories(username)

    sorted_repos = sorted(
        repos,
        key=lambda x: x["stargazers_count"],
        reverse=True
    )

    return {
        "username": profile["login"],
        "bio": profile["bio"],
        "followers": profile["followers"],
        "following": profile["following"],
        "public_repositories": profile["public_repos"],
        "account_created": profile["created_at"],
        "most_active_repositories": [
            repo["name"] for repo in sorted_repos[:5]
        ]
    }