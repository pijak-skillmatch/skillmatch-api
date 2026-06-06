from datetime import datetime, timezone
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
)
from app.db.database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    name = Column(
        String,
        nullable=False,
    )

    email = Column(
        String,
        unique=True,
        nullable=False,
        index=True,
    )

    password_hash = Column(
        String,
        nullable=False,
    )

    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
    )
