def test_receipt_crud_and_list(client, sale):
    payload = {
        "sale_id": sale["sale_id"],
        "receipt_number": "R-100",
        "type": "sales_receipt",
        "receipt_data": "receipt body",
    }
    created = client.post("/receipt/", json=payload)
    assert created.status_code == 201, created.text
    receipt = created.json()
    receipt_id = receipt["receipt_id"]
    assert receipt["receipt_number"] == "R-100"
    assert receipt["type"] == "sales_receipt"

    listed = client.get("/receipt/")
    assert listed.status_code == 200
    assert any(row["receipt_id"] == receipt_id for row in listed.json())

    fetched = client.get(f"/receipt/{receipt_id}")
    assert fetched.status_code == 200
    assert fetched.json()["sale_id"] == sale["sale_id"]

    updated = client.put(
        f"/receipt/{receipt_id}",
        json={"receipt_number": "R-101", "type": "return_ticket", "receipt_data": "updated"},
    )
    assert updated.status_code == 200
    assert updated.json()["receipt_number"] == "R-101"
    assert updated.json()["type"] == "return_ticket"

    assert client.delete(f"/receipt/{receipt_id}").status_code == 204
    assert client.get(f"/receipt/{receipt_id}").status_code == 404


def test_receipt_validation_and_missing_resource(client, sale):
    assert client.post("/receipt/", json={}).status_code == 422
    assert client.post(
        "/receipt/",
        json={
            "sale_id": sale["sale_id"],
            "receipt_number": "R-invalid",
            "type": "not-a-valid-type",
            "receipt_data": "x",
        },
    ).status_code == 422
    assert client.get("/receipt/not-a-uuid").status_code == 422
    assert client.get("/receipt/00000000-0000-0000-0000-000000000000").status_code == 404


def test_duplicate_receipt_number_is_rejected_by_database(client, sale):
    payload = {
        "sale_id": sale["sale_id"],
        "receipt_number": "R-DUP",
        "type": "sales_receipt",
        "receipt_data": "x",
    }
    assert client.post("/receipt/", json=payload).status_code == 201
    response = client.post("/receipt/", json=payload)
    assert response.status_code == 500
