
def test_user_all(http_client):
    response = http_client.get("public/v2/users")
    assert response.status_code == 200

def test_create_user(http_client):
    http_client.post("/public/v2/users", {"name": "Jane", "email": "abhaya_chopra@schaden.org", "gender": "male", "status": "active"})


def test_change_user (http_client):
    http_client.put("/public/v2/users/7", {"name": "John"})

def test_delete_user (http_client):
    http_client.delete("/public/v2/users/7")
