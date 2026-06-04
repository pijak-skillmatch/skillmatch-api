from fastapi import APIRouter

from app.core.artifacts import artifacts

router = APIRouter()


@router.get("/health")
def health_check():

    return {
        "status": "healthy",
        "artifacts_loaded":
            artifacts.industry_model is not None
    }