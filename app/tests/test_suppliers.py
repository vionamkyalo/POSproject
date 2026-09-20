def test_supplier_crud_and_list(client):
    payload = {
        "company_name": "Pixie dolls",
        "contact_name": "Princess",
        "email": "princess@pixie.test",
        "supplier_phone": "0712345678",
        "address": "Garden city",
    }
    created = client.post("/supplier/", json=payload)
    assert created.status_code == 201
    supplier = created.json()
    supplier_id = supplier["supplier_id"]
    assert supplier["company_name"] == "Pixie dolls"
    assert supplier["is_active"] is True

    listed = client.get("/supplier/")
    assert listed.status_code == 200
    assert any(item["supplier_id"] == supplier_id for item in listed.json())

    fetched = client.get(f"/supplier/{supplier_id}")
    assert fetched.status_code == 200
    assert fetched.json()["email"] == payload["email"]

    updated = client.put(f"/supplier/{supplier_id}", json={"company_name": "Pixie dolls", "is_active": False})
    assert updated.status_code == 200
    assert updated.json()["company_name"] == "Pixie dolls"
    assert updated.json()["is_active"] is False

    assert client.delete(f"/supplier/{supplier_id}").status_code == 204
    assert client.get(f"/supplier/{supplier_id}").status_code == 404


def test_supplier_validation_and_missing_resource(client):
    assert client.post("/supplier/", json={}).status_code == 422
    assert client.get("/supplier/not-a-uuid").status_code == 422
    assert client.get("/supplier/00000000-0000-0000-0000-000000000000").status_code == 404


def test_duplicate_supplier_email_is_rejected_by_database(client):
    payload = {"company_name": "One", "email": "duplicate@example.com"}
    assert client.post("/supplier/", json=payload).status_code == 201
    response = client.post("/supplier/", json={"company_name": "Two", "email": payload["email"]})
    assert response.status_code == 500
