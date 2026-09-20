from pydantic import BaseModel, Field
from typing import Optional

class ProductBase(BaseModel):
    name: str = Field(..., examples=["Pen"])
    brand: str = Field(..., examples=["Bic"])
    selling_price: float = Field(..., examples=[20.0])
    buying_price: float = Field(..., examples=[12.5])
    stock_quantity: int = Field(..., examples=[100])
    category_id: int = Field(..., examples=[1])
    supplier_id: int = Field(..., examples=[1])


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    brand: Optional[str] = None
    selling_price: Optional[float] = None
    buying_price: Optional[float] = None
    stock_quantity: Optional[int] = None
    category_id: Optional[int] = None
    supplier_id: Optional[int] = None


class ProductRead(ProductBase):
    id: int

    class Config:
        from_attributes = True