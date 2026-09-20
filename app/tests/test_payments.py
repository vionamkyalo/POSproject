from datetime import datetime, timezone


def test_payment_crud_list_and_status_filter(client, sale):
    payload = {
        "sale_id": sale["sale_id"],
        "payment_method": "cash",
        "amount": "105.00",
        "payment_date": datetime.now(timezone.utc).isoformat(),
        "status": "completed",
    }
    created = client.post("/payment/", json=payload)
    assert created.status_code == 201, created.text
    payment = created.json()
    payment_id = payment["payment_id"]

    listed = client.get("/payment/")
    assert listed.status_code == 200
    assert any(row["payment_id"] == payment_id for row in listed.json())

    fetched = client.get(f"/payment/{payment_id}")
    assert fetched.status_code == 200
    assert fetched.json()["payment_method"] == "cash"

    filtered = client.get("/payment/status/completed")
    assert filtered.status_code == 200
    assert any(row["payment_id"] == payment_id for row in filtered.json())

    updated = client.put(f"/payment/{payment_id}", json={"status": "refunded", "payment_method": "credit_card"})
    assert updated.status_code == 200
    assert updated.json()["status"] == "refunded"
    assert updated.json()["payment_method"] == "credit_card"

    assert client.delete(f"/payment/{payment_id}").status_code == 204
    assert client.get(f"/payment/{payment_id}").status_code == 404


def test_payment_validation_and_missing_resource(client):
    assert client.post("/payment/", json={}).status_code == 422
    assert client.get("/payment/not-a-uuid").status_code == 422
    assert client.get("/payment/00000000-0000-0000-0000-000000000000").status_code == 404
