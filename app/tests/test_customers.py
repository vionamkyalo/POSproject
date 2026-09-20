def test_category_crud_and_list(client):
    created = client.post("/category/", json={"name": "Drinks", "description": "Beverages"})
    assert created.status_code == 201
    category = created.json()
    category_id = category["category_id"]
    assert category["name"] == "Drinks"
    assert category["is_active"] is True

    listed = client.get("/category/")
    assert listed.status_code == 200
    assert any(item["category_id"] == category_id for item in listed.json())

    fetched = client.get(f"/category/{category_id}")
    assert fetched.status_code == 200
    assert fetched.json()["description"] == "Beverages"

    updated = client.put(f"/category/{category_id}", json={"name": "Cold Drinks", "is_active": False})
    assert updated.status_code == 200
    assert updated.json()["name"] == "Cold Drinks"
    assert updated.json()["is_active"] is False

    deleted = client.delete(f"/category/{category_id}")
    assert deleted.status_code == 204
    assert client.get(f"/category/{category_id}").status_code == 404


def test_category_validation_and_missing_resource(client):
    assert client.post("/category/", json={}).status_code == 422
    assert client.get("/category/not-a-uuid").status_code == 422
    assert client.get("/category/00000000-0000-0000-0000-000000000000").status_code == 404
