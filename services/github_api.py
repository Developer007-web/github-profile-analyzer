import os
import httpx
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

BASE_URL = "https://api.github.com"


class GitHubAPI:

    def __init__(self):

        self.headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {GITHUB_TOKEN}"
        }

    async def get_user(self, username: str):

        url = f"{BASE_URL}/users/{username}"

        async with httpx.AsyncClient() as client:

            response = await client.get(
                url,
                headers=self.headers
            )

        if response.status_code != 200:
            raise Exception(
                f"GitHub API Error: {response.status_code}"
            )

        return response.json()

    async def get_repositories(self, username: str):

        url = f"{BASE_URL}/users/{username}/repos?per_page=100"

        async with httpx.AsyncClient() as client:

            response = await client.get(
                url,
                headers=self.headers
            )

        if response.status_code != 200:
            raise Exception(
                f"GitHub Repo Error: {response.status_code}"
            )

        return response.json()