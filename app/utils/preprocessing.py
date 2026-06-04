def preprocess_skills(
    skills: list[str]
) -> list[str]:

    return list(
        {
            skill.lower().strip()
            for skill in skills
        }
    )