from tempfile import (
    NamedTemporaryFile,
)

from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Form,
)

from app.services.resume_analysis_service import (
    analyze_resume_profile,
)

router = APIRouter()


@router.post(
    "/resume/analyze"
)
async def analyze_resume(

    resume: UploadFile = File(
        ...
    ),

    experience: str = Form(
        ...
    ),
):

    with NamedTemporaryFile(
        delete=False,
        suffix=".pdf",
    ) as temp_file:

        content = await resume.read()

        temp_file.write(
            content
        )

        temp_path = (
            temp_file.name
        )

    result = (
        analyze_resume_profile(
            pdf_path=temp_path,
            experience=experience,
        )
    )

    return {
        "success": True,
        "data": result,
    }