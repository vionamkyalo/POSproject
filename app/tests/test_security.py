from app.core.security import (
    create_access_token,
    hash_password,
    verify_password,
)


def test_hash_and_verify_password():
    password = "testpassword"

    hashed_password = hash_password(password)
    
    assert isinstance(hashed_password, str)
    assert hashed_password != password
    assert verify_password(password, hashed_password) is True


def test_create_access_token():
    user_id = 1

    token = create_access_token(user_id)

    assert isinstance(token, str)
    assert token