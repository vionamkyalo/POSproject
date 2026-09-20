from sqlalchemy import Column, Float, ForeignKey, Integer

# Make sure this line is present:
from database import Base


class SaleItem(Base):
    __tablename__ = "sale_items"
    __table_args__ = {"extend_existing": True}

    sales_item_id = Column(Integer, primary_key=True)  # index=True is removed
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Integer, nullable=False)
    total_price = Column(Float, nullable=False)
