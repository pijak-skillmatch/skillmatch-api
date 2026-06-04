from fastapi import FastAPI

from app.core.config import (
    APP_NAME,
    API_VERSION
)

from app.api.health import (
    router as health_router
)

app = FastAPI(
    title=APP_NAME,
    version=API_VERSION
)

app.include_router(
    health_router,
    prefix="/api/v1"
)

@app.get("/")
def root():

    return {
        "message": "SkillMatch AI API"
    }