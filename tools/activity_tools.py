from services.github_api import GitHubAPI
from services.analyzer import Analyzer

api = GitHubAPI()


async def activity_score(username: str):

    repos = await api.get_repositories(username)

    return Analyzer.activity_score(repos)


async def learning_rate(username: str):

    repos = await api.get_repositories(username)

    return Analyzer.learning_rate(repos)