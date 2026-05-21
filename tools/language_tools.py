from services.github_api import GitHubAPI
from services.analyzer import Analyzer

api = GitHubAPI()


async def analyze_languages(username: str):

    repos = await api.get_repositories(username)

    return Analyzer.analyze_languages(repos)