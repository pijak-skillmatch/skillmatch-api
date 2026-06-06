from datetime import (
    datetime,
    timedelta,
)

from jose import jwt
import bcrypt

from app.core.config import (
    SECRET_KEY,
    ALGORITHM,
    ACCESS_TOKEN_EXPIRE_MINUTES,
)


def hash_password(
    password: str,
) -> str:

    hashed = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt(),
    )

    return hashed.decode("utf-8")


def verify_password(
    plain_password: str,
    hashed_password: str,
) -> bool:

    return bcrypt.checkpw(
        plain_password.encode("utf-8"),
        hashed_password.encode("utf-8"),
    )


def create_access_token(
    subject: str,
) -> str:

    expire = (
        datetime.utcnow()
        + timedelta(
            minutes=
            ACCESS_TOKEN_EXPIRE_MINUTES
        )
    )

    payload = {
        "sub": subject,
        "exp": expire,
    }

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM,
    )