from services.github_api import GitHubAPI
from services.analyzer import Analyzer

api = GitHubAPI()


async def repo_insights(username: str):

    repos = await api.get_repositories(username)

    return Analyzer.repo_insights(repos)