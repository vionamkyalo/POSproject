from sqlalchemy.orm import Session
from app.models.user import User

class UserRepository:
    def __init__(self):
        self.model = User

    def get(self, db: Session, id: int):
        return db.query(self.model).filter(self.model.user_id == id).first()

    def get_all(self, db: Session):
        return db.query(self.model).all()

    def create(self, db: Session, data: dict):
        user = self.model(**data)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    def update(self, db: Session, db_obj: User, obj_in: dict):
        for field, value in obj_in.items():
            setattr(db_obj, field, value)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, db_obj: User):
        db.delete(db_obj)
        db.commit()
        return db_obj

user_repository = UserRepository()