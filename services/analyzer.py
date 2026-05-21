from collections import Counter
from datetime import datetime

from utils.helpers import (
    calculate_percentages,
    detect_primary_stack
)


class Analyzer:

    @staticmethod
    def analyze_languages(repos):
        language_counter = Counter()

        for repo in repos:
            language = repo.get("language")

            if language:
                language_counter[language] += 1

        percentages = calculate_percentages(language_counter)

        return {
            "languages": dict(language_counter),
            "percentages": percentages,
            "primary_stack": detect_primary_stack(percentages)
        }

    @staticmethod
    def repo_insights(repos):

        most_starred = max(
            repos,
            key=lambda x: x["stargazers_count"],
            default=None
        )

        most_forked = max(
            repos,
            key=lambda x: x["forks_count"],
            default=None
        )

        largest_repo = max(
            repos,
            key=lambda x: x["size"],
            default=None
        )

        inactive = []

        for repo in repos:
            updated = datetime.strptime(
                repo["updated_at"],
                "%Y-%m-%dT%H:%M:%SZ"
            )

            days = (datetime.utcnow() - updated).days

            if days > 180:
                inactive.append(repo["name"])

        return {
            "most_starred": most_starred["name"] if most_starred else None,
            "most_forked": most_forked["name"] if most_forked else None,
            "largest_repo": largest_repo["name"] if largest_repo else None,
            "inactive_repositories": inactive
        }

    @staticmethod
    def activity_score(repos):

        total_updates = 0

        for repo in repos:
            updated = datetime.strptime(
                repo["updated_at"],
                "%Y-%m-%dT%H:%M:%SZ"
            )

            days = (datetime.utcnow() - updated).days

            if days <= 30:
                total_updates += 10
            elif days <= 90:
                total_updates += 5

        score = min(total_updates, 100)

        return {
            "activity_score": score,
            "activity_level": (
                "High" if score > 70
                else "Medium" if score > 40
                else "Low"
            )
        }

    @staticmethod
    def learning_rate(repos):

        old_repos = repos[:len(repos)//2]
        new_repos = repos[len(repos)//2:]

        old_languages = set(
            repo["language"]
            for repo in old_repos
            if repo["language"]
        )

        new_languages = set(
            repo["language"]
            for repo in new_repos
            if repo["language"]
        )

        learned = list(new_languages - old_languages)

        return {
            "newly_learned_technologies": learned,
            "learning_trend": (
                "Growing Fast"
                if len(learned) >= 3
                else "Steady"
            )
        }