from sqlalchemy.orm import Session
from app.models.payment import Payment

class PaymentRepository:
    def __init__(self):
        self.model = Payment

    def get(self, db: Session, id: int):
        return db.query(self.model).filter(self.model.payment_id == id).first()

    def get_all(self, db: Session):
        return db.query(self.model).all()

    def create(self, db: Session, data: dict):
        payment = self.model(**data)
        db.add(payment)
        db.commit()
        db.refresh(payment)
        return payment

    def update(self, db: Session, db_obj: Payment, obj_in: dict):
        for field, value in obj_in.items():
            setattr(db_obj, field, value)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, db_obj: Payment):
        db.delete(db_obj)
        db.commit()
        return db_obj

payment_repository = PaymentRepository()