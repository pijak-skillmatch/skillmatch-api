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

FRONTEND_URL = os.getenv(
    "FRONTEND_URL",
    "http://localhost:3000"
)

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///./skillmatch.db"
)

ALLOWED_ORIGINS = [

    "http://localhost:3000",

    "http://127.0.0.1:3000",

    FRONTEND_URL,

]

SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "your-secret-key"
)

ALGORITHM = os.getenv(
    "ALGORITHM",
    "HS256"
)

ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv(
        "ACCESS_TOKEN_EXPIRE_MINUTES",
        "1440"
    )
)