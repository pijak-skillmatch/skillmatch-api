from pathlib import Path
from typing import Any

import joblib
import pickle

BASE_DIR = Path(__file__).resolve().parent.parent.parent

ARTIFACT_DIR = BASE_DIR / "artifacts"


class ArtifactManager:

    tfidf: Any
    industry_model: Any

    skill_gap_engine: dict[str, Any] | None
    metadata: dict[str, Any] | None

    def __init__(self):

        self.tfidf = None
        self.industry_model = None

        self.skill_gap_engine = None
        self.metadata = None

    def load(self):

        self.tfidf = joblib.load(
            ARTIFACT_DIR / "industry_tfidf.pkl"
        )

        self.industry_model = joblib.load(
            ARTIFACT_DIR / "industry_classifier.pkl"
        )

        with open(
            ARTIFACT_DIR / "skill_gap_engine.pkl",
            "rb"
        ) as f:

            self.skill_gap_engine = pickle.load(f)

        with open(
            ARTIFACT_DIR / "metadata.pkl",
            "rb"
        ) as f:

            self.metadata = pickle.load(f)

        print("Artifacts loaded successfully")


artifacts = ArtifactManager()