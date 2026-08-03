from datetime import datetime
from pydantic import BaseModel, ConfigDict

class PaymentBase(BaseModel):
    sales_id: int
    payment_method: str
    amount_paid: float

class PaymentCreate(PaymentBase):
    pass

class PaymentUpdate(BaseModel):
    sales_id: int | None = None
    payment_method: str | None = None
    amount_paid: float | None = None

class PaymentRead(PaymentBase):
    payment_id: int
    payment_date: datetime

    model_config = ConfigDict(from_attributes=True)