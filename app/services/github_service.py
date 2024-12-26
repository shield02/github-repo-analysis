from typing import List
import requests

userUrl = 'https://github.com/username'

class GitHubApi:
    """A utility for interacting with GitHub API."""
    BASE_URL = "https://api.github.com"

    def __init__(self, token: str):
        """Class constructor."""
        self.headers = {"Authorization": f"token {token}"}

    async def fetch_user_repositories(self, userUrl: str) -> List[dict]:
        """Fetch repositories by username."""
        username = userUrl.split('/')[-1]

        url = f"{self.BASE_URL}/users/{username}/repos"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()

        # if response.status_code == 200:
        #     return response
        # else:
        #     raise Exception(f"Failed to fetch repositories: {response.status_code}")

        return response
