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
    status = response.status_code

    assert status == 201
    assert data["phone"] == payload["phone"]
    assert "password" not in data


# @pytest.mark.django_db
# def test_create_jwt(user):

#     response_jwt = client.post("/auth/jwt/create/", dict(phone="111919191", password="liverpool", re_password="liverpool"))
#     status_jwt = response_jwt.status_code

#     assert status_jwt == 200

@pytest.mark.django_db
def test_create_test(order_test):



    assert order_test == 1