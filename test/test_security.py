from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
)

password = "12345678"

hashed = hash_password(
    password
)

print(
    "HASH:",
    hashed
)

print(
    "VERIFY:",
    verify_password(
        password,
        hashed,
    )
)

token = create_access_token(
    "test@example.com"
)

print(
    "TOKEN:",
    token
)