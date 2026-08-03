from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from database import get_db
from app.schemas.category import CategoryCreate, CategoryUpdate, CategoryRead
from app.services import category

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.get("/", response_model=list[CategoryRead])
def list_categories(db: Session = Depends(get_db)):
    return category.list_categories(db)

@router.get("/{category_id}", response_model=CategoryRead)
def get_category(category_id: int, db: Session = Depends(get_db)):
    return category.get_category(db, category_id)

@router.post("/", response_model=CategoryRead, status_code=status.HTTP_201_CREATED)
def create_category(data: CategoryCreate, db: Session = Depends(get_db)):
    return category.create_category(db, data)

@router.put("/{category_id}", response_model=CategoryRead)
def update_category(category_id: int, data: CategoryUpdate, db: Session = Depends(get_db)):
    return category.update_category(db, category_id, data)

@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    category.delete_category(db, category_id)