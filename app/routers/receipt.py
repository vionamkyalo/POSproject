from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from app.schemas.receipt import ReceiptCreate, ReceiptUpdate, ReceiptRead
from app.services.receipt import get_receipt, list_receipts, create_receipt, update_receipt, delete_receipt

router = APIRouter(prefix="/receipts", tags=["Receipts"])

@router.get("/", response_model=list[ReceiptRead])
def list_receipts_route(db: Session = Depends(get_db)):
    return list_receipts(db)

@router.get("/{id}", response_model=ReceiptRead)
def get_receipt_route(id: int, db: Session = Depends(get_db)):
    return get_receipt(db, id)

@router.post("/", response_model=ReceiptRead, status_code=status.HTTP_201_CREATED)
def create_receipt_route(data: ReceiptCreate, db: Session = Depends(get_db)):
    return create_receipt(db, data)

@router.put("/{id}", response_model=ReceiptRead)
def update_receipt_route(id: int, data: ReceiptUpdate, db: Session = Depends(get_db)):
    return update_receipt(db, id, data)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_receipt_route(id: int, db: Session = Depends(get_db)):
    return delete_receipt(db, id)