from typing import List
import requests


class GitHubApi:
    """A utility for interacting with GitHub API."""
    BASE_URL = "https://api.github.com"

    def __init__(self, token: str):
        """Class constructor."""
        self.headers = {"Authorization": f"token {token}"}

    async def fetch_repositories(self, username: str) -> List[dict]:
        """Fetch repositories by username."""
        url = f"{self.BASE_URL}/users/{username}/repos"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

