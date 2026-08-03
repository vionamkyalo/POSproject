from pydantic import BaseModel, ConfigDict

class SaleItemBase(BaseModel):
    product_id: int
    quantity: int
    unit_price: int
    total_price: float

class SaleItemCreate(SaleItemBase):
    pass

class SaleItemUpdate(BaseModel):
    product_id: int | None = None
    quantity: int | None = None
    unit_price: int | None = None
    total_price: float | None = None

class SaleItemRead(SaleItemBase):
    sales_item_id: int

    model_config = ConfigDict(from_attributes=True)