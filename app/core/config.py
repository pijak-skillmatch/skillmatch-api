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

ALLOWED_ORIGINS = [

    "http://localhost:3000",

    "http://127.0.0.1:3000",

    FRONTEND_URL,

]