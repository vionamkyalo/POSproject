from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db


from app.schemas.sale_item import SaleItemCreate, SaleItemUpdate, SaleItemRead
from app.services.sale_item import (
    get_sale_item,
    list_sale_items,
    create_sale_item,
    update_sale_item,
    delete_sale_item,
)

router = APIRouter(prefix="/sale-items", tags=["Sale Items"])


@router.get("/", response_model=list[SaleItemRead])
def list_sale_items_route(db: Session = Depends(get_db)):
    return list_sale_items(db)


@router.get("/{sales_item_id}", response_model=SaleItemRead)
def get_sale_item_route(sales_item_id: int, db: Session = Depends(get_db)):
    db_sale_item = get_sale_item(db, sales_item_id)
    if not db_sale_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sale item not found"
        )
    return db_sale_item


@router.post("/", response_model=SaleItemRead, status_code=status.HTTP_201_CREATED)
def create_sale_item_route(data: SaleItemCreate, db: Session = Depends(get_db)):
    return create_sale_item(db, data)


@router.put("/{sales_item_id}", response_model=SaleItemRead)
def update_sale_item_route(
    sales_item_id: int, data: SaleItemUpdate, db: Session = Depends(get_db)
):
    db_sale_item = update_sale_item(db, sales_item_id, data)
    if not db_sale_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sale item not found"
        )
    return db_sale_item


@router.delete("/{sales_item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_sale_item_route(sales_item_id: int, db: Session = Depends(get_db)):
    success = delete_sale_item(db, sales_item_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sale item not found"
        )
    return None