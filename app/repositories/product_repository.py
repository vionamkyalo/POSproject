from sqlalchemy.orm import Session
from app.models.product import Product

class ProductRepository:
    def __init__(self):
        self.model = Product

    def get(self, db: Session, id: int):
        return db.query(self.model).filter(self.model.id == id).first()

    def get_all(self, db: Session):
        return db.query(self.model).all()

    def create(self, db: Session, data: dict):
        product = self.model(**data)
        db.add(product)
        db.commit()
        db.refresh(product)
        return product

    def update(self, db: Session, db_obj: Product, obj_in: dict):
        for field, value in obj_in.items():
            setattr(db_obj, field, value)
        db.commit()
        db.refresh(db_obj)
        return db_obj


    def remove_product(db: Session, db_obj: Product):
        db.delete(db_obj)
        db.commit()
        return db_obj


product_repository = ProductRepository()