from sqlalchemy import Column, Integer, String, Float, ForeignKey
from database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String, nullable=False)
    brand = Column(String, nullable=False)
    selling_price = Column(Float, nullable=False)
    buying_price = Column(Float, nullable=False)
    stock_quantity = Column(Integer, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.category_id"), nullable=False)
    supplier_id = Column(Integer, ForeignKey("suppliers.supplier_id"), nullable=False)