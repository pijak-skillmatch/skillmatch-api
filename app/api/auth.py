from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)

from sqlalchemy.orm import Session

from app.db.database import (
    get_db,
)

from fastapi.security import (
    OAuth2PasswordRequestForm,
)

from app.schemas.auth import (
    RegisterRequest,
    TokenResponse,
)

from app.services.auth_service import (
    register_user,
    login_user,
)

from app.models.user import User

from app.core.dependencies import (
    get_current_user,
)

router = APIRouter()


@router.post(
    "/register",
)
def register(
    payload: RegisterRequest,
    db: Session = Depends(
        get_db
    ),
):

    try:

        user = register_user(
            db,
            payload,
        )

        return {
            "success": True,
            "message":
                "User registered successfully",
            "data": {
                "id": user.id,
                "name": user.name,
                "email": user.email,
            },
        }

    except ValueError as error:

        raise HTTPException(
            status_code=400,
            detail=str(error),
        )


@router.post(
    "/login",
    response_model=TokenResponse,
)
def login(
    form_data:
    OAuth2PasswordRequestForm =
    Depends(),

    db: Session =
    Depends(get_db),
):
    try:

        token = login_user(
            db=db,
            email=form_data.username,
            password=form_data.password,
        )

        return TokenResponse(
            access_token=token
        )

    except ValueError as error:

        raise HTTPException(
            status_code=401,
            detail=str(error),
        )

@router.get(
    "/me"
)
def get_me(
    current_user: User = Depends(
        get_current_user
    ),
):

    return {
        "id": current_user.id,
        "name": current_user.name,
        "email": current_user.email,
    }