from fastapi import APIRouter

from app.schemas.request import (
    AnalyzeRequest,
)

from app.schemas.response import (
    AnalyzeResponse,
)

from app.services.analysis_service import (
    analyze_profile,
)

router = APIRouter()


@router.post(
    "/analyze",
    response_model=AnalyzeResponse,
)
def analyze(
    request: AnalyzeRequest,
):

    result = analyze_profile(
        skills=request.skills,
        experience=request.experience,
    )

    return {
        "success": True,
        "data": result,
    }