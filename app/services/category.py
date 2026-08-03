from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.repositories.category_repository import category_repository
from app.schemas.category import CategoryCreate, CategoryUpdate

def get_category(db: Session, id: int):
    category = category_repository.get(db, id)
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found"
        )
    return category

def list_categories(db: Session):
    return category_repository.get_all(db)

def create_category(db: Session, data: CategoryCreate):
    return category_repository.create(db, data.model_dump())

def update_category(db: Session, id: int, data: CategoryUpdate):
    category = get_category(db, id)
    return category_repository.update(db, category, data.model_dump(exclude_unset=True))

def delete_category(db: Session, id: int):
    category = get_category(db, id)
    return category_repository.remove(db, category)