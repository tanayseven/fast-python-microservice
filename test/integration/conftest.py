from typing import Generator

import pytest
import requests
from fastapi.testclient import TestClient
from requests.adapters import HTTPAdapter
from urllib3 import Retry  # type: ignore

from src.main import app


@pytest.fixture(scope="function", autouse=True)
def wait_for_api(function_scoped_container_getter) -> (requests.Session, str):
    """Wait for the api from my_api_service to become responsive"""
    request_session = requests.Session()
    retries = Retry(total=5, backoff_factor=0.1, status_forcelist=[500, 502, 503, 504])
    request_session.mount("http://", HTTPAdapter(max_retries=retries))

    service = function_scoped_container_getter.get("adminer").network_info[0]
    api_url = "http://%s:%s/" % (service.hostname, service.host_port)
    assert request_session.get(api_url)
    return request_session, api_url


@pytest.fixture
def client() -> Generator[TestClient, None, None]:
    yield TestClient(app=app)
