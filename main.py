from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.artifacts import artifacts

from app.api.health import router as health_router

from app.api.debug import (
    router as debug_router
)


@asynccontextmanager
async def lifespan(app: FastAPI):

    artifacts.load()

    yield


app = FastAPI(
    title="SkillMatch AI API",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(
    health_router,
    prefix="/api/v1"
)

app.include_router(
    debug_router,
    prefix="/api/v1/debug"
)