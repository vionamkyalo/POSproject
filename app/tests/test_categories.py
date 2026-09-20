def test_category_crud_and_list(client):
    create_payload = {
        "category_name": "Drinks",
        "description": "Beverages",
    }

    created = client.post("/categories/", json=create_payload)

    assert created.status_code == 201

    created_data = created.json()

    assert created_data["category_name"] == "Drinks"
    assert created_data["description"] == "Beverages"
    assert "category_id" in created_data

    category_id = created_data["category_id"]

    listed = client.get("/categories/")

    assert listed.status_code == 200

    categories = listed.json()

    assert len(categories) == 1
    assert categories[0]["category_id"] == category_id
    assert categories[0]["category_name"] == "Drinks"

    retrieved = client.get(f"/categories/{category_id}")

    assert retrieved.status_code == 200
    assert retrieved.json()["category_id"] == category_id
    assert retrieved.json()["category_name"] == "Drinks"
    assert retrieved.json()["description"] == "Beverages"

    updated = client.put(
        f"/categories/{category_id}",
        json={
            "category_name": "Cold Drinks",
            "description": "Chilled beverages",
        },
    )

    assert updated.status_code == 200
    assert updated.json()["category_id"] == category_id
    assert updated.json()["category_name"] == "Cold Drinks"
    assert updated.json()["description"] == "Chilled beverages"

    deleted = client.delete(f"/categories/{category_id}")

    assert deleted.status_code == 204

    missing_after_delete = client.get(f"/categories/{category_id}")

    assert missing_after_delete.status_code == 404


def test_category_validation_and_missing_resource(client):
    invalid_create = client.post("/categories/", json={})

    assert invalid_create.status_code == 422

    missing_get = client.get("/categories/99999")

    assert missing_get.status_code == 404

    missing_update = client.put(
        "/categories/99999",
        json={
            "category_name": "Does Not Exist",
            "description": "No category exists with this ID",
        },
    )

    assert missing_update.status_code == 404

    missing_delete = client.delete("/categories/99999")

    assert missing_delete.status_code == 404