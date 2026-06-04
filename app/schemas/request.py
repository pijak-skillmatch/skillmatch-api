from pydantic import (
    BaseModel,
    Field,
)


class AnalyzeRequest(
    BaseModel
):

    skills: list[str] = Field(
        ...,
        min_length=1,
        max_length=20,
    )

    experience: str = Field(
        ...,
        min_length=1,
    )