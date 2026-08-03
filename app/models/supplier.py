from sqlalchemy import Column, Integer, String
from database import Base

class Supplier(Base):
    __tablename__ = "suppliers"

    supplier_id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String, nullable=False)
    contact_name = Column(String, nullable=True)
    phone_number = Column(String, nullable=False)
    email = Column(String, nullable=True)