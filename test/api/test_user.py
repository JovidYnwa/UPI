import pytest
from rest_framework.test import APIClient

client = APIClient()

@pytest.mark.django_db
def test_register_user():
    payload = dict(
        phone= "111919191",
        password= "pass@123",
        re_password= "pass@123",
    )
    response = client.post("/auth/users/", payload)
    data = response.data

    assert data["phone"] == payload["phone"]
    assert "password" not in data
