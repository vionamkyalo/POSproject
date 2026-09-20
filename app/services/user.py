from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.user_repository import user_repository
from app.schemas.user import UserCreate, UserUpdate
from app.services.auth_service import hash_password


def get_user(db: Session, id: int):
    user = user_repository.get(db, id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    return user


def list_users(db: Session):
    return user_repository.get_all(db)


def register(db: Session, data: UserCreate):
    existing_user = user_repository.get_by_username(
        db,
        data.username,
    )

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already taken",
        )

    values = data.model_dump()

    raw_password = values.pop("password")
    values["hashed_password"] = hash_password(raw_password)

    return user_repository.create(db, values)


def create_user(db: Session, data: UserCreate):
    return register(db, data)


def update_user(db: Session, id: int, data: UserUpdate):
    db_user = get_user(db, id)

    values = data.model_dump(exclude_unset=True)

    if "password" in values and values["password"]:
        raw_password = values.pop("password")
        values["hashed_password"] = hash_password(raw_password)

    return user_repository.update(
        db,
        db_user,
        values,
    )


def delete_user(db: Session, id: int):
    db_user = get_user(db, id)

    return user_repository.remove(db, db_user)
