def test_register_and_login(client, user_payload):
    response = client.post("/auth/register", json=user_payload)

    assert response.status_code == 201

    registered_user = response.json()

    assert registered_user["username"] == user_payload["username"]
    assert "user_id" in registered_user

    login_response = client.post(
        "/auth/login",
        json={
            "username": user_payload["username"],
            "password": user_payload["password"],
        },
    )

    assert login_response.status_code == 200

    token_data = login_response.json()

    assert token_data["token_type"] == "bearer"
    assert "access_token" in token_data
    assert token_data["access_token"]


def test_duplicate_username_is_rejected(client, user_payload):
    first_response = client.post("/auth/register", json=user_payload)

    assert first_response.status_code == 201

    duplicate_response = client.post("/auth/register", json=user_payload)

    assert duplicate_response.status_code == 400


def test_invalid_login_is_rejected(client, user_payload):
    created = client.post("/auth/register", json=user_payload)

    assert created.status_code == 201

    response = client.post(
        "/auth/login",
        json={
            "username": user_payload["username"],
            "password": "wrong-password",
        },
    )

    assert response.status_code == 401


def test_login_requires_username_and_password(client):
    response = client.post("/auth/login", json={})

    assert response.status_code == 422


def test_inactive_user_cannot_login(client, user_payload):
    created = client.post("/auth/register", json=user_payload)

    assert created.status_code == 201

    user_id = created.json()["user_id"]

    updated = client.put(
        f"/users/{user_id}",
        json={
            "is_active": False,
        },
    )

    assert updated.status_code == 200

    login_response = client.post(
        "/auth/login",
        json={
            "username": user_payload["username"],
            "password": user_payload["password"],
        },
    )

    assert login_response.status_code == 400


def test_products_endpoint_is_available(client):
    response = client.get("/products/")

    assert response.status_code == 200


def test_products_endpoint_does_not_require_auth(client):
    response = client.get(
        "/products/",
        headers={
            "Authorization": "Bearer invalid-token",
        },
    )

    assert response.status_code == 200