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


def build_learning_path(
    user_skills: list[str],
    target_industry: str,
):

    engine = get_engine()

    skill_tiers = engine.get(
        "skill_tiers",
        {},
    )

    industry_tiers = skill_tiers.get(
        target_industry,
        {},
    )

    roadmap = []

    for level, skills in (
        industry_tiers.items()
    ):

        remaining_skills = [
            skill
            for skill in skills
            if skill not in user_skills
        ]

        roadmap.append(
            {
                "level": level,
                "skills": remaining_skills,
            }
        )

    return roadmap