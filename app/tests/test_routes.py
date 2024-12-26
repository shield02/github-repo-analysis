from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

user_url = "https://github.com/username"

def test_url_is_valid():
    response = client.post("/analyze", json={"github_user_url": user_url})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data["test_repo"], dict)
