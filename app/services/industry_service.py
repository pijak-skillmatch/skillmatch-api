import pandas as pd

from app.core.artifacts import artifacts
from app.core.exceptions import (
    SkillMatchException,
)


def predict_industries(
    skills: list[str],
    experience: str,
) -> pd.DataFrame:

    if artifacts.tfidf is None:
        raise SkillMatchException(
            "TF-IDF artifact not loaded"
        )

    if artifacts.industry_model is None:
        raise SkillMatchException(
            "Industry model artifact not loaded"
        )

    text = (
        " ".join(skills)
        + " "
        + experience.lower()
    )

    vector = artifacts.tfidf.transform(
        [text]
    )

    probabilities = (
        artifacts.industry_model
        .predict_proba(vector)[0]
    )

    results = pd.DataFrame(
        {
            "industry": artifacts.industry_model.classes_,
            "probability": probabilities.astype(float),
        }
    )

    return results.sort_values(
        by="probability",
        ascending=False,
    ).reset_index(drop=True)