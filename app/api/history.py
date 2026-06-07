from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)

from sqlalchemy.orm import Session

from app.db.database import (
    get_db,
)

from app.models.user import User

from app.core.dependencies import (
    get_current_user,
)

from app.schemas.history_schema import (
    AnalysisHistoryCreate,
    AnalysisHistoryResponse,
    AnalysisHistoryDetail,
)

from app.services.history_service import (
    create_history,
    get_user_histories,
    get_history_by_id,
    delete_history,
)

router = APIRouter()


@router.post("")
def save_history(
    payload: AnalysisHistoryCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    ),
):

    history = create_history(
        db=db,
        user_id=int(current_user.id),
        history_data=payload,
    )

    return {
        "success": True,
        "message":
            "History saved successfully",
        "data": {
            "id": history.id,
        },
    }


@router.get(
    "",
    response_model=list[
        AnalysisHistoryResponse
    ]
)
def get_histories(
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    ),
):

    return get_user_histories(
        db=db,
        user_id=int(current_user.id),
    )


@router.get(
    "/{history_id}",
    response_model=
    AnalysisHistoryDetail,
)
def get_history(
    history_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    ),
):

    history = get_history_by_id(
        db=db,
        history_id=history_id,
        user_id=int(current_user.id),
    )

    if not history:

        raise HTTPException(
            status_code=404,
            detail="History not found",
        )

    return history


@router.delete(
    "/{history_id}"
)
def remove_history(
    history_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    ),
):

    deleted = delete_history(
        db=db,
        history_id=history_id,
        user_id=int(current_user.id),
    )

    if not deleted:

        raise HTTPException(
            status_code=404,
            detail="History not found",
        )

    return {
        "success": True,
        "message":
            "History deleted successfully",
    }