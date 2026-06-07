from datetime import datetime

from pydantic import BaseModel


class AnalysisHistoryCreate(
    BaseModel
):

    analysis_type: str

    industry: str

    confidence: float

    input_skills: list[str] | None = None

    result_json: dict


class AnalysisHistoryResponse(
    BaseModel
):

    id: int

    analysis_type: str

    industry: str

    confidence: float

    created_at: datetime

    class Config:

        from_attributes = True


class AnalysisHistoryDetail(
    BaseModel
):

    id: int

    analysis_type: str

    industry: str

    confidence: float

    input_skills: list[str] | None = None

    result_json: dict

    created_at: datetime

    class Config:

        from_attributes = True