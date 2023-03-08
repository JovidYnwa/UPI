import pytest
from rest_framework.test import APIClient

client = APIClient()

@pytest.mark.django_db
#To access the database in a test you need to inject a special fixture called db.
def test_register_user(user):


    assert user.phone == "111919192"
    # assert data["phone"] == payload["phone"]
    # assert "password" not in data


@pytest.mark.django_db
def test_create_jwt(user):
    print("======> ", user.phone)
    print("======> ", user.phone)

    response_jwt = client.post("/auth/jwt/create/", dict(phone="111919192", password="test@123"))
    status_jwt = response_jwt.status_code

    assert status_jwt == 200

# @pytest.mark.django_db
# def test_create_test():

#     order_test == 1

#     assert order_test == 1