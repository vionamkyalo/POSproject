import os

TEST_DATABASE_URL = "sqlite:///./pos_test.db"

os.environ["DATABASE_URL"] = TEST_DATABASE_URL

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database import Base, get_db

from main import app


test_engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=test_engine,
)


@pytest.fixture()
def db():
    Base.metadata.drop_all(bind=test_engine)
    Base.metadata.create_all(bind=test_engine)

    session = TestingSessionLocal()

    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(bind=test_engine)


@pytest.fixture()
def client(db):
    def override_get_db():
        try:
            yield db
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app, raise_server_exceptions=True) as test_client:
        yield test_client

    app.dependency_overrides.clear()


@pytest.fixture()
def user_payload():
    return {
        "username": "testuser",
        "password": "testpassword",
        "first_name": "Test",
        "last_name": "User",
        "email": "test@example.com",
        "role": "cashier",
    }


@pytest.fixture()
def registered_user(client, user_payload):
    response = client.post("/auth/register", json=user_payload)
    assert response.status_code == 201, response.text
    return response.json()


@pytest.fixture()
def auth_headers(client, user_payload, registered_user):
    response = client.post(
        "/auth/login",
        json={
            "username": user_payload["username"],
            "password": user_payload["password"],
        },
    )

    assert response.status_code == 200, response.text

    return {
        "Authorization": f"Bearer {response.json()['access_token']}"
    }


@pytest.fixture()
def category(client):
    response = client.post(
        "/category/",
        json={
            "name": "Drinks",
            "description": "Beverages",
        },
    )

    assert response.status_code == 201, response.text
    return response.json()


@pytest.fixture()
def supplier(client):
    response = client.post(
        "/supplier/",
        json={
            "company_name": "Acme Supplies",
            "contact_name": "Sam",
            "email": "sam@acme.test",
            "supplier_phone": "555-0100",
        },
    )

    assert response.status_code == 201, response.text
    return response.json()


@pytest.fixture()
def customer(client):
    response = client.post(
        "/customer/",
        json={
            "first_name": "Jane",
            "last_name": "Doe",
        },
    )

    assert response.status_code == 201, response.text
    return response.json()


@pytest.fixture()
def app_user(client):
    response = client.post(
        "/user/",
        json={
            "username": "cashier",
            "password": "password123",
            "first_name": "Cash",
            "last_name": "Ier",
            "email": "cashier@example.com",
            "role": "cashier",
        },
    )

    assert response.status_code == 201, response.text
    return response.json()


@pytest.fixture()
def sale(client, customer, app_user):
    from datetime import datetime, timezone

    response = client.post(
        "/sale/",
        json={
            "customer_id": customer["customer_id"],
            "user_id": app_user["user_id"],
            "sale_date": datetime.now(timezone.utc).isoformat(),
            "subtotal": "100.00",
            "tax_amount": "10.00",
            "discount_amount": "5.00",
            "total_amount": "105.00",
            "status": "completed",
        },
    )

    assert response.status_code == 201, response.text
    return response.json()


@pytest.fixture()
def product(client, auth_headers, category, supplier):
    response = client.post(
        "/product/",
        headers=auth_headers,
        json={
            "name": "Coca Cola",
            "price": "100.00",
            "quantity": 10,
            "category_id": category["category_id"],
            "supplier_id": supplier["supplier_id"],
        },
    )

    assert response.status_code == 201, response.text
    return response.json()