from app.services.resume_service import (
    analyze_resume,
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

from app.utils.preprocessing import (
    preprocess_skills,
)


def analyze_resume_profile(
    pdf_path: str,
    experience: str,
):

    resume_result = (
        analyze_resume(
            pdf_path
        )
    )

    skills = (
        resume_result[
            "detected_skills"
        ]
    )

    skills = preprocess_skills(
        skills
    )

    if len(skills) == 0:

        return {
            "detected_skills": [],
            "industry_predictions": [],
            "recommended_skills": [],
            "learning_path": [],
        }

    industry_df = (
        predict_industries(
            skills=skills,
            experience=experience,
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

        "detected_skills":
            skills,

        "industry_predictions":
            industry_df.head(3)
            .to_dict(
                orient="records"
            ),

        "recommended_skills":
            recommendations,

        "learning_path":
            learning_path,

    }