def test_user_crud_and_list(client):
    payload = {
        "username": "manager",
        "password": "secret123",
        "first_name": "Store",
        "last_name": "Manager",
        "email": "manager@example.com",
        "role": "store_manager",
    }
    created = client.post("/user/", json=payload)
    assert created.status_code == 201
    user = created.json()
    user_id = user["user_id"]
    assert user["username"] == "manager"
    assert "password" not in user
    assert user["role"] == "store_manager"

    listed = client.get("/user/")
    assert listed.status_code == 200
    assert any(item["user_id"] == user_id for item in listed.json())

    fetched = client.get(f"/user/{user_id}")
    assert fetched.status_code == 200
    assert fetched.json()["email"] == payload["email"]

    updated = client.put(f"/user/{user_id}", json={"first_name": "Updated", "role": "cashier"})
    assert updated.status_code == 200
    assert updated.json()["first_name"] == "Updated"
    assert updated.json()["role"] == "cashier"

    assert client.delete(f"/user/{user_id}").status_code == 204
    assert client.get(f"/user/{user_id}").status_code == 404


def test_user_validation_and_missing_resource(client):
    assert client.post("/user/", json={}).status_code == 422
    assert client.post(
        "/user/",
        json={
            "username": "ab",
            "password": "short",
            "first_name": "A",
            "last_name": "B",
            "email": "a@example.com",
            "role": "cashier",
        },
    ).status_code == 422
    assert client.get("/user/not-a-uuid").status_code == 422
    assert client.get("/user/00000000-0000-0000-0000-000000000000").status_code == 404
