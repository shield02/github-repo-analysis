from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.github_service import GitHubApi

router = APIRouter()

class AnalysisRequest(BaseModel):
    github_user_url: str

@router.post("/analyze")
async def analyze_repositories(request: AnalysisRequest):
    try:
        repos = GitHubApi.fetch_user_repositories(request.github_user_url)
        if not repos:
            raise HTTPException(
                status_code=404,
                detail="No repositories found"
            )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
