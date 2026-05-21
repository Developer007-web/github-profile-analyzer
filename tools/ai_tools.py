from services.github_api import GitHubAPI
from services.analyzer import Analyzer
from services.ai_service import AIService

api = GitHubAPI()


async def generate_summary(username: str):

    profile = await api.get_user(username)
    repos = await api.get_repositories(username)

    lang_data = Analyzer.analyze_languages(repos)

    return {
        "summary": AIService.generate_summary(
            profile,
            lang_data
        )
    }


async def github_roast(username: str):

    profile = await api.get_user(username)

    return {
        "roast": AIService.roast(profile)
    }


async def project_recommendations(username: str):

    repos = await api.get_repositories(username)

    lang_data = Analyzer.analyze_languages(repos)

    return {
        "recommended_projects":
            AIService.project_recommendations(
                lang_data["primary_stack"]
            )
    }