from datetime import datetime
from pydantic import BaseModel, ConfigDict

class ReceiptBase(BaseModel):
    sale_id: int
    receipt_number: str
    receipt_date: datetime

class ReceiptCreate(ReceiptBase):
    pass

class ReceiptUpdate(BaseModel):
    sale_id: int | None = None
    receipt_number: str | None = None
    receipt_date: datetime | None = None

class ReceiptRead(ReceiptBase):
    id: int

    model_config = ConfigDict(from_attributes=True)