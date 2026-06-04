from contextlib import asynccontextmanager

from fastapi import FastAPI

from fastapi.middleware.cors import (
    CORSMiddleware,
)

from app.api.health import (
    router as health_router,
)

from app.api.debug import (
    router as debug_router,
)

from app.api.analyze import (
    router as analyze_router,
)

from app.api.skills import (
    router as skills_router,
)

from app.api.resume import (
    router as resume_router,
)

from app.core.artifacts import (
    artifacts,
)

from app.core.handlers import (
    skillmatch_exception_handler,
)

from app.core.exceptions import (
    SkillMatchException,
)

from app.core.config import (
    APP_NAME,
    API_VERSION,
    ALLOWED_ORIGINS,
)


@asynccontextmanager
async def lifespan(
    app: FastAPI,
):

    artifacts.load()

    print(
        "Application startup completed"
    )

    yield

    print(
        "Application shutdown"
    )


app = FastAPI(

    title=APP_NAME,

    description=(
        "Industry Recommendation "
        "and Skill Gap Analysis API"
    ),

    version=API_VERSION,

    lifespan=lifespan,

)

# -------------------------------
# CORS
# -------------------------------

app.add_middleware(

    CORSMiddleware,

    allow_origins=ALLOWED_ORIGINS,

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],

)

# -------------------------------
# Exception Handler
# -------------------------------

app.add_exception_handler(
    SkillMatchException,
    skillmatch_exception_handler,
)

# -------------------------------
# Routers
# -------------------------------

app.include_router(
    health_router,
    prefix="/api/v1",
    tags=["Health"],
)

app.include_router(
    debug_router,
    prefix="/api/v1/debug",
    tags=["Debug"],
)

app.include_router(
    analyze_router,
    prefix="/api/v1",
    tags=["Analysis"],
)

app.include_router(
    skills_router,
    prefix="/api/v1",
    tags=["Skills"],
)

app.include_router(
    resume_router,
    prefix="/api/v1",
    tags=["Resume"],
)

# -------------------------------
# Root Endpoint
# -------------------------------

@app.get("/")
def root():

    return {
        "message":
        "SkillMatch AI API"
    }