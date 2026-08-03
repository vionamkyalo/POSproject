from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.sql import func
from database import Base

class Payment(Base):
    __tablename__ = "payments"

    payment_id = Column(Integer, primary_key=True, index=True)
    sales_id = Column(Integer, ForeignKey("sales.sales_id"), nullable=False)
    payment_method = Column(String, nullable=False)
    amount_paid = Column(Float, nullable=False)
    payment_date = Column(DateTime, server_default=func.now(), nullable=False)