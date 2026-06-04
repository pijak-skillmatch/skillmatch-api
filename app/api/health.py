from fastapi import APIRouter

from app.core.artifacts import (
    artifacts,
)

router = APIRouter()


@router.get("/health")
def health_check():

    return {
        "status": "healthy",

        "artifacts_loaded":
            bool(
                artifacts.skill_gap_engine
            ),

        "version":
            "1.0.0",
    }