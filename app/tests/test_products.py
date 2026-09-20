def test_product_crud_with_category_and_supplier(client, auth_headers, category, supplier):
    payload = {
        "name": "Coca Cola",
        "price": "100.00",
        "quantity": 10,
        "category_id": category["category_id"],
        "supplier_id": supplier["supplier_id"],
        "barcode": "123456789",
    }
    created = client.post("/product/", json=payload, headers=auth_headers)
    assert created.status_code == 201, created.text
    product = created.json()
    product_id = product["product_id"]
    assert product["name"] == "Coca Cola"
    assert product["price"] == "100.00"

    listed = client.get("/product/", headers=auth_headers)
    assert listed.status_code == 200
    assert any(item["product_id"] == product_id for item in listed.json())

    fetched = client.get(f"/product/{product_id}", headers=auth_headers)
    assert fetched.status_code == 200
    assert fetched.json()["category_id"] == category["category_id"]
    assert fetched.json()["supplier_id"] == supplier["supplier_id"]

    updated = client.put(
        f"/product/{product_id}",
        json={"name": "Pepsi", "price": "120.00", "quantity": 20},
        headers=auth_headers,
    )
    assert updated.status_code == 200
    assert updated.json()["name"] == "Pepsi"
    assert updated.json()["quantity"] == 20

    assert client.delete(f"/product/{product_id}", headers=auth_headers).status_code == 204
    assert client.get(f"/product/{product_id}", headers=auth_headers).status_code == 404


def test_product_validation_and_missing_resource(client, auth_headers):
    assert client.post("/product/", json={"name": "Missing price"}, headers=auth_headers).status_code == 422
    assert client.get("/product/not-a-uuid", headers=auth_headers).status_code == 422
    assert client.get(
        "/product/00000000-0000-0000-0000-000000000000", headers=auth_headers
    ).status_code == 404
