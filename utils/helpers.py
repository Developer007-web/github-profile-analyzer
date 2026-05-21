from collections import Counter


def calculate_percentages(language_data):
    total = sum(language_data.values())

    if total == 0:
        return {}

    return {
        lang: round((count / total) * 100, 2)
        for lang, count in language_data.items()
    }


def detect_primary_stack(percentages):
    sorted_langs = sorted(
        percentages.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return [lang for lang, _ in sorted_langs[:5]]