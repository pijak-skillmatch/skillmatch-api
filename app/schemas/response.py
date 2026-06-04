from pydantic import BaseModel


class IndustryPrediction(BaseModel):

    industry: str

    probability: float


class SkillRecommendation(BaseModel):

    skill: str

    score: float

    reasons: list[str]


class LearningPathItem(BaseModel):

    level: str

    skills: list[str]


class AnalyzeData(BaseModel):

    industry_predictions: list[
        IndustryPrediction
    ]

    recommended_skills: list[
        SkillRecommendation
    ]

    learning_path: list[
        LearningPathItem
    ]


class AnalyzeResponse(BaseModel):

    success: bool

    data: AnalyzeData