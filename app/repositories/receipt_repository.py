from sqlalchemy.orm import Session
from app.models.receipt import Receipt

class ReceiptRepository:
    def __init__(self):
        self.model = Receipt

    def get(self, db: Session, id: int):
        return db.query(self.model).filter(self.model.id == id).first()

    def get_all(self, db: Session):
        return db.query(self.model).all()

    def create(self, db: Session, data: dict):
        receipt = self.model(**data)
        db.add(receipt)
        db.commit()
        db.refresh(receipt)
        return receipt

    def update(self, db: Session, db_obj: Receipt, obj_in: dict):
        for field, value in obj_in.items():
            setattr(db_obj, field, value)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, db_obj: Receipt):
        db.delete(db_obj)
        db.commit()
        return db_obj

receipt_repository = ReceiptRepository()