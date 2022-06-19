from tests.conftest import http_client

def test_user_by_id(http_client):
    response = http_client.get("public/v2/users/7")
    assert response.status_code == 200