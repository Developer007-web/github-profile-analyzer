class AIService:

    @staticmethod
    def generate_summary(profile, lang_data):

        stack = ", ".join(lang_data["primary_stack"])

        return f"""
Developer {profile['login']} is experienced in {stack}.

They have {profile['public_repos']} public repositories
and a growing GitHub presence with
{profile['followers']} followers.
"""

    @staticmethod
    def roast(profile):

        repos = profile["public_repos"]

        if repos < 5:
            return "Your GitHub profile is emptier than a fresh VS Code install."

        if repos < 20:
            return "You start projects faster than you finish them."

        return "You probably rename final_final_v2 files daily."

    @staticmethod
    def project_recommendations(stack):

        recommendations = {
            "Python": [
                "AI Resume Analyzer",
                "Automation Dashboard"
            ],
            "JavaScript": [
                "Realtime Chat App",
                "AI Code Reviewer"
            ],
            "Java": [
                "Banking System",
                "Spring Boot API"
            ]
        }

        output = []

        for tech in stack:
            output.extend(recommendations.get(tech, []))

        return list(set(output))