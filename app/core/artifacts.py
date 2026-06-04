from pathlib import Path
from typing import Any

import joblib
import pickle


BASE_DIR = Path(__file__).resolve().parent.parent.parent

ARTIFACT_DIR = BASE_DIR / "artifacts"


class ArtifactManager:

    def __init__(self):

        self.tfidf: Any = None

        self.industry_model: Any = None

        self.skill_gap_engine: dict[str, Any] = {}
        
        self.metadata: dict[str, Any] = {}

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