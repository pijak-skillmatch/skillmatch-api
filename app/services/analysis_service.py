from app.utils.preprocessing import (
    preprocess_skills,
)

from app.services.industry_service import (
    predict_industries,
)

from app.services.skill_gap_service import (
    recommend_skill_gap_explainable,
)

from app.services.learning_path_service import (
    build_learning_path,
)


def analyze_profile(
    skills: list[str],
    experience: str,
):

    skills = preprocess_skills(
        skills
    )

    industry_df = (
        predict_industries(
            skills,
            experience,
        )
    )

    if industry_df.empty:
        raise RuntimeError(
            "Industry prediction failed"
        )

    top_industry = str(
        industry_df.iloc[0][
            "industry"
        ]
    )

    recommendations = (
        recommend_skill_gap_explainable(
            user_skills=skills,
            target_industry=top_industry,
            top_n=5,
        )
    )

    learning_path = (
        build_learning_path(
            user_skills=skills,
            target_industry=top_industry,
        )
    )

    return {
        "industry_predictions": (
            industry_df.head(3)
            .to_dict(
                orient="records"
            )
        ),
        "recommended_skills":
            recommendations,
        "learning_path":
            learning_path,
    }