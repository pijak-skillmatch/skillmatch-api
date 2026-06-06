from sqlalchemy.orm import Session

from app.models.user import User

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
)

from app.schemas.auth import (
    RegisterRequest,
)


def register_user(
    db: Session,
    payload: RegisterRequest,
):

    existing_user = (
        db.query(User)
        .filter(
            User.email ==
            payload.email
        )
        .first()
    )

    if existing_user:

        raise ValueError(
            "Email already registered"
        )

    user = User(
        name=payload.name,
        email=payload.email,
        password_hash=hash_password(
            payload.password
        ),
    )

    db.add(user)

    db.commit()

    db.refresh(user)

    return user


def login_user(
    db: Session,
    email: str,
    password: str,
):

    user = (
        db.query(User)
        .filter(
            User.email == email
        )
        .first()
    )

    if not user:

        raise ValueError(
            "Invalid credentials"
        )

    if not verify_password(
        password,
        str(user.password_hash),
    ):

        raise ValueError(
            "Invalid credentials"
        )

    return create_access_token(
        str(user.email)
    )