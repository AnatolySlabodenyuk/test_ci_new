import pytest
from nickname import app, FUNNY_NICKNAMES  # импорт из nickname.py

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_nickname_route(client):
    response = client.get("/nickname")
    assert response.status_code == 200

    data = response.get_json()
    assert "nickname" in data
    assert data["nickname"] in FUNNY_NICKNAMES
