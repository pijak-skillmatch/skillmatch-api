from datetime import (
    datetime,
    timezone,
)

from sqlalchemy import (
    Float,
    String,
    DateTime,
    ForeignKey,
    JSON,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from app.db.database import Base


class AnalysisHistory(Base):

    __tablename__ = "analysis_history"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )

    analysis_type: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    industry: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    confidence: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    input_skills: Mapped[list | None] = mapped_column(
        JSON,
        nullable=True,
    )

    result_json: Mapped[dict] = mapped_column(
        JSON,
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda:
        datetime.now(timezone.utc),
    )