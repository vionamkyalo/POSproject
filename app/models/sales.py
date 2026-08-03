from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.sql import func
from database import Base

class Sale(Base):
    __tablename__ = "sales"

    sales_id = Column(Integer, primary_key=True, index=True)
    sale_date = Column(DateTime, server_default=func.now(), nullable=False)
    total_amount = Column(Float, nullable=False)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"), nullable=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)