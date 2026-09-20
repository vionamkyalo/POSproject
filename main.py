from fastapi import FastAPI

from app.routers import (
    auth,
    category,
    customer,
    payment,
    products,
    receipt,
    sale_item,
    sales,
    supplier,
    user,
)

app = FastAPI(
    title="Store API Management System",
)

app.include_router(auth.router)
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
    return {
        "message": "API is working successfully",
    }