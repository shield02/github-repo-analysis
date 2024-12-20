from pydantic import BaseModel


class Repository(BaseModel):
    """Define a model to represent the repository data fetched from GitHub."""
    name: str
    description: str
    language: str
    size: int
    url: str
    stargazers_count: int
    forks_count: int
    contributors_count: int
