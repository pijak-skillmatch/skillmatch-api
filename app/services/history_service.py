from sqlalchemy.orm import Session

from app.models.analysis_history import (
    AnalysisHistory,
)

from app.schemas.history_schema import (
    AnalysisHistoryCreate,
)


def create_history(
    db: Session,
    user_id: int,
    history_data:
    AnalysisHistoryCreate,
):

    history = AnalysisHistory(
        user_id=user_id,

        analysis_type=
        history_data.analysis_type,

        industry=
        history_data.industry,

        confidence=
        history_data.confidence,

        input_skills=
        history_data.input_skills,

        result_json=
        history_data.result_json,
    )

    db.add(history)

    db.commit()

    db.refresh(history)

    return history


def get_user_histories(
    db: Session,
    user_id: int,
):

    return (
        db.query(
            AnalysisHistory
        )
        .filter(
            AnalysisHistory.user_id
            == user_id
        )
        .order_by(
            AnalysisHistory.created_at
            .desc()
        )
        .all()
    )


def get_history_by_id(
    db: Session,
    history_id: int,
    user_id: int,
):

    return (
        db.query(
            AnalysisHistory
        )
        .filter(
            AnalysisHistory.id
            == history_id,

            AnalysisHistory.user_id
            == user_id,
        )
        .first()
    )


def delete_history(
    db: Session,
    history_id: int,
    user_id: int,
):

    history = (
        db.query(
            AnalysisHistory
        )
        .filter(
            AnalysisHistory.id
            == history_id,

            AnalysisHistory.user_id
            == user_id,
        )
        .first()
    )

    if not history:
        return False

    db.delete(history)

    db.commit()

    return True