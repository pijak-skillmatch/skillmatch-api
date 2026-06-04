from fastapi import APIRouter

from app.core.artifacts import artifacts

router = APIRouter()


@router.get("/artifacts")
def artifact_info():

    if (
        artifacts.skill_gap_engine is None
        or artifacts.metadata is None
    ):
        return {
            "loaded": False
        }

    return {
        "loaded": True,
        "skills": len(
            artifacts.skill_gap_engine[
                "skill_vocabulary"
            ]
        ),
        "industries":
            artifacts.metadata["industries"],
        "version":
            artifacts.metadata["version"],
    }