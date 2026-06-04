from app.core.artifacts import artifacts
from app.core.exceptions import (
    SkillMatchException,
)


def get_engine() -> dict:

    engine = artifacts.skill_gap_engine

    if not engine:
        raise SkillMatchException(
            "Skill gap engine not loaded"
        )

    return engine

def get_industry_reason(
    skill: str,
    industry: str,
) -> str | None:

    engine = get_engine()

    industry_df = engine.get(
        "industry_skill_freq_df"
    )

    if industry_df is None:
        return None

    row = industry_df[
        (industry_df["industry"] == industry)
        &
        (industry_df["skill"] == skill)
    ]

    if row.empty:
        return None

    frequency = float(
        row.iloc[0]["frequency"]
    )

    return (
        f"Appears in "
        f"{frequency:.1%} of "
        f"{industry} profiles"
    )

def get_industry_skill_gap(
    user_skills: list[str],
    target_industry: str,
):

    engine = get_engine()

    industry_skill_freq_df = engine.get(
        "industry_skill_freq_df"
    )

    if industry_skill_freq_df is None:
        raise SkillMatchException(
            "industry_skill_freq_df not found"
        )

    filtered = industry_skill_freq_df[
        industry_skill_freq_df["industry"]
        == target_industry
    ].copy()

    filtered = filtered[
        ~filtered["skill"].isin(
            user_skills
        )
    ]

    return filtered

def get_association_reasons(
    target_skill: str,
    user_skills: list[str],
    top_n: int = 3,
):

    engine = get_engine()

    association_df = engine.get(
        "association_df"
    )

    if association_df is None:
        return []

    reasons = []

    for skill in user_skills:

        rules = association_df[
            (association_df["antecedent"] == skill)
            &
            (
                association_df["consequent"]
                == target_skill
            )
        ]

        if rules.empty:
            continue

        lift = float(
            rules.iloc[0]["lift"]
        )

        reasons.append(
            (
                skill,
                lift,
            )
        )

    reasons.sort(
        key=lambda x: x[1],
        reverse=True,
    )

    return reasons[:top_n]

def association_scores(
    user_skills: list[str],
):

    engine = get_engine()

    association_df = engine.get(
        "association_df"
    )

    if association_df is None:
        raise SkillMatchException(
            "association_df not found"
        )

    scores = {}

    for skill in user_skills:

        rules = association_df[
            association_df["antecedent"]
            == skill
        ]

        for _, row in rules.iterrows():

            target_skill = row[
                "consequent"
            ]

            if target_skill in user_skills:
                continue

            scores[target_skill] = (
                scores.get(
                    target_skill,
                    0,
                )
                + float(row["lift"])
            )

    return scores

def explain_recommendation(
    skill: str,
    user_skills: list[str],
    industry: str,
):

    explanations = []

    industry_reason = (
        get_industry_reason(
            skill,
            industry,
        )
    )

    if industry_reason:
        explanations.append(
            industry_reason
        )

    associations = (
        get_association_reasons(
            skill,
            user_skills,
        )
    )

    for (
        source_skill,
        lift,
    ) in associations:

        explanations.append(
            f"Strong association with "
            f"{source_skill} "
            f"(lift={lift:.2f})"
        )

    return explanations


def recommend_skill_gap(
    user_skills: list[str],
    target_industry: str,
    top_n: int = 5,
    industry_weight: float = 0.6,
    association_weight: float = 0.4,
):

    industry_df = (
        get_industry_skill_gap(
            user_skills,
            target_industry,
        )
    )

    association_score_map = (
        association_scores(
            user_skills
        )
    )

    recommendations = []

    for _, row in industry_df.iterrows():

        skill = row["skill"]

        industry_score = float(
            row["frequency"]
        )

        association_score = float(
            association_score_map.get(
                skill,
                0,
            )
        )

        final_score = (
            industry_weight
            * industry_score
            + association_weight
            * association_score
        )

        recommendations.append(
            {
                "skill": skill,
                "score": round(
                    final_score,
                    4,
                ),
                "industry_score": round(
                    industry_score,
                    4,
                ),
                "association_score": round(
                    association_score,
                    4,
                ),
            }
        )

    recommendations.sort(
        key=lambda x: x["score"],
        reverse=True,
    )

    return recommendations[:top_n]

def recommend_skill_gap_explainable(
    user_skills: list[str],
    target_industry: str,
    top_n: int = 5,
):

    recommendations = (
        recommend_skill_gap(
            user_skills=user_skills,
            target_industry=target_industry,
            top_n=top_n,
        )
    )

    results = []

    for item in recommendations:

        results.append(
            {
                "skill": item["skill"],
                "score": item["score"],
                "reasons": (
                    explain_recommendation(
                        skill=item["skill"],
                        user_skills=user_skills,
                        industry=target_industry,
                    )
                ),
            }
        )

    return results