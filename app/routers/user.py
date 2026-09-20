from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from database import get_db
from app.schemas.user import UserCreate, UserUpdate, UserRead
from app.services.user import (
    get_user,
    list_users,
    create_user,
    update_user,
    delete_user,
)


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get(
    "/",
    response_model=list[UserRead],
)
def list_users_route(
    db: Session = Depends(get_db),
):
    return list_users(db)


@router.get(
    "/{user_id}",
    response_model=UserRead,
)
def get_user_route(
    user_id: int,
    db: Session = Depends(get_db),
):
    return get_user(db, user_id)


@router.post(
    "/",
    response_model=UserRead,
    status_code=status.HTTP_201_CREATED,
)
def create_user_route(
    data: UserCreate,
    db: Session = Depends(get_db),
):
    return create_user(db, data)


@router.put(
    "/{user_id}",
    response_model=UserRead,
)
def update_user_route(
    user_id: int,
    data: UserUpdate,
    db: Session = Depends(get_db),
):
    return update_user(db, user_id, data)


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_user_route(
    user_id: int,
    db: Session = Depends(get_db),
):
    delete_user(db, user_id)