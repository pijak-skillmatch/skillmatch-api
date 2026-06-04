from dotenv import load_dotenv

import os

load_dotenv()

APP_NAME = os.getenv(
    "APP_NAME",
    "SkillMatch AI API"
)

API_VERSION = os.getenv(
    "API_VERSION",
    "1.0.0"
)