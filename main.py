
from fastapi import FastAPI
from database import engine, Base
from app.models.product import Product
from app.models.customer import Customer
from app.models.user import User
from app.models.sales import Sale
from app.models.sale_item import SaleItem
from app.models.payment import Payment
from app.models.category import Category
from app.models.supplier import Supplier
from app.models.receipt import Receipt
Base.metadata.clear()
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
app = FastAPI(title="Store API Management System")
from app.routers import (
    products,
    customer,
    user,
    sales,
    sale_item,
    payment,
    category,
    supplier,
    receipt
)
app.include_router(products.router)
app.include_router(customer.router)
app.include_router(user.router)
app.include_router(sales.router)
app.include_router(sale_item.router)
app.include_router(payment.router)
app.include_router(category.router)
app.include_router(supplier.router)
app.include_router(receipt.router)
@app.get("/")
def root():
    return {"message": "API is working successfully"}