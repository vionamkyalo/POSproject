from sqlalchemy.orm import Session
from app.repositories.sale_item_repository import sale_item_repository

def get_sale_item(db: Session, sale_item_id: int):
    return sale_item_repository.get(db, id=sale_item_id)

def list_sale_items(db: Session):
    return sale_item_repository.get_all(db)

def create_sale_item(db: Session, data: dict):
    return sale_item_repository.create(db, data=data)

def update_sale_item(db: Session, db_obj, obj_in: dict):
    return sale_item_repository.update(db, db_obj=db_obj, obj_in=obj_in)

def delete_sale_item(db: Session, db_obj):
    return sale_item_repository.remove(db, db_obj=db_obj)