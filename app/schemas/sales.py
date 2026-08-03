from datetime import datetime
from pydantic import BaseModel, ConfigDict

class SaleBase(BaseModel):
    total_amount: float
    customer_id: int | None = None
    user_id: int

class SaleCreate(SaleBase):
    pass

class SaleUpdate(BaseModel):
    total_amount: float | None = None
    customer_id: int | None = None
    user_id: int | None = None

class SaleRead(SaleBase):
    sales_id: int
    sale_date: datetime

    model_config = ConfigDict(from_attributes=True)