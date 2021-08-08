from fastapi.testclient import TestClient


def test_login(client: TestClient) -> None:
    response = client.post(f"/user/login")
    assert response.json() == {"message": "login successful"}


def test_sign_up(client: TestClient) -> None:
    response = client.post(f"/user/sign-up")
    assert response.json() == {"message": "sign up successful"}
