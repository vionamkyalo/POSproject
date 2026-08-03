from sqlalchemy.orm import Session
from app.models.customer import Customer

class CustomerRepository:
    def __init__(self):
        self.model = Customer

    def get(self, db: Session, id: int):
        return db.query(self.model).filter(self.model.customer_id == id).first()

    def get_all(self, db: Session):
        return db.query(self.model).all()

    def create(self, db: Session, data: dict):
        customer = self.model(**data)
        db.add(customer)
        db.commit()
        db.refresh(customer)
        return customer

    def update(self, db: Session, db_obj: Customer, obj_in: dict):
        for field, value in obj_in.items():
            setattr(db_obj, field, value)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, db_obj: Customer):
        db.delete(db_obj)
        db.commit()
        return db_obj

customer_repository = CustomerRepository()