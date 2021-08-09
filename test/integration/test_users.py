from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from src.users.db_tables import User


def test_login_success(client: TestClient, db: Session) -> None:
    user = User(username="john.doe", password="password", email="john.doe@company.com")
    db.add(user)
    db.commit()

    response = client.post(
        f"/user/login", json={"username": "john.doe", "password": "password"}
    )

    assert response.json() == {"message": "login successful"}


def test_sign_up(client: TestClient) -> None:
    response = client.post(f"/user/sign-up")
    assert response.json() == {"message": "sign up successful"}
