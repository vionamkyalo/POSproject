from sqlalchemy.orm import Session
from app.models.category import Category

class CategoryRepository:
    def __init__(self):
        self.model = Category

    def get(self, db: Session, id: int):
        return db.query(self.model).filter(self.model.category_id == id).first()

    def get_all(self, db: Session):
        return db.query(self.model).all()

    def create(self, db: Session, data: dict):
        category = self.model(**data)
        db.add(category)
        db.commit()
        db.refresh(category)
        return category

    def update(self, db: Session, db_obj: Category, obj_in: dict):
        for field, value in obj_in.items():
            setattr(db_obj, field, value)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, db_obj: Category):
        db.delete(db_obj)
        db.commit()
        return db_obj

category_repository = CategoryRepository()