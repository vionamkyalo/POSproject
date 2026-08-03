from pydantic import BaseModel, ConfigDict

class SupplierBase(BaseModel):
    company_name: str
    contact_name: str | None = None
    phone_number: str
    email: str | None = None

class SupplierCreate(SupplierBase):
    pass

class SupplierUpdate(BaseModel):
    company_name: str | None = None
    contact_name: str | None = None
    phone_number: str | None = None
    email: str | None = None

class SupplierRead(SupplierBase):
    supplier_id: int

    model_config = ConfigDict(from_attributes=True)