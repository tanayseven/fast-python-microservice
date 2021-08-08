from pathlib import Path

from fastapi.testclient import TestClient


def test_file_upload(client: TestClient) -> None:
    some_file = "some-file.txt"
    with open(Path(".") / "test" / "data" / some_file, "r") as file_handler:
        file_to_be_uploaded = {"file": (some_file, file_handler, "text/plain")}
        response = client.post("/file/upload", files=file_to_be_uploaded)
        assert response.json() == {"message": f"{some_file} successfully uploaded"}
