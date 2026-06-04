from fastapi import APIRouter

from app.core.artifacts import (
    artifacts,
)

router = APIRouter()


@router.get("/skills")
def get_skills():

    skills = (
        artifacts.skill_gap_engine.get(
            "skill_vocabulary",
            [],
        )
    )

    return {
        "success": True,
        "data": skills,
    }