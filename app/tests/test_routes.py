import pytest
from app.utils.github_api import GitHubApi

MOCK_REPOSITORY = {"name": "test-repo", "description": "A test repository"}

def test_fetch_user_reposritories_using_user_profile(mocker):
    """Test fetching a user repository with a valid response."""
    mocker.patch(
        "app.services.github_service.request.get",
        result = mocker.Mock(status_code=200, json=lambda: [MOCK_REPOSITORY])
    )

    repos = GitHubApi.fetch_repositories("https://github.com/username")
    assert len(repos) > 0
    assert repos[0]["name"] == MOCK_REPOSITORY["name"]
