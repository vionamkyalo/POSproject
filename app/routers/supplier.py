from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from app.schemas.supplier import SupplierCreate, SupplierUpdate, SupplierRead
from app.services.supplier import get_supplier, list_suppliers, create_supplier, update_supplier, delete_supplier

router = APIRouter(prefix="/suppliers", tags=["Suppliers"])

@router.get("/", response_model=list[SupplierRead])
def list_suppliers_route(db: Session = Depends(get_db)):
    return list_suppliers(db)

@router.get("/{id}", response_model=SupplierRead)
def get_supplier_route(id: int, db: Session = Depends(get_db)):
    return get_supplier(db, id)

@router.post("/", response_model=SupplierRead, status_code=status.HTTP_201_CREATED)
def create_supplier_route(data: SupplierCreate, db: Session = Depends(get_db)):
    return create_supplier(db, data)

@router.put("/{id}", response_model=SupplierRead)
def update_supplier_route(id: int, data: SupplierUpdate, db: Session = Depends(get_db)):
    return update_supplier(db, id, data)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_supplier_route(id: int, db: Session = Depends(get_db)):
    return delete_supplier(db, id)