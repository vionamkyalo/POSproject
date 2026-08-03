from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from app.schemas.sales import SaleCreate, SaleUpdate, SaleRead


from app.services.sales import get_sale, list_sales, create_sale, update_sale, delete_sale

router = APIRouter(prefix="/sales", tags=["Sales"])

@router.get("/", response_model=list[SaleRead])
def list_sales_route(db: Session = Depends(get_db)):
    return list_sales(db)

@router.get("/{sales_id}", response_model=SaleRead)
def get_sale_route(sales_id: int, db: Session = Depends(get_db)):
    return get_sale(db, sales_id)

@router.post("/", response_model=SaleRead, status_code=status.HTTP_201_CREATED)
def create_sale_route(data: SaleCreate, db: Session = Depends(get_db)):
    return create_sale(db, data)

@router.put("/{sales_id}", response_model=SaleRead)
def update_sale_route(sales_id: int, data: SaleUpdate, db: Session = Depends(get_db)):
    return update_sale(db, sales_id, data)

@router.delete("/{sales_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_sale_route(sales_id: int, db: Session = Depends(get_db)):
    return delete_sale(db, sales_id)