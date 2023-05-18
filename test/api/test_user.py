import pytest
from rest_framework.test import APIClient

client = APIClient()

@pytest.mark.django_db
#To access the database in a test you need to inject a special fixture called db.
def test_register_user(user):
    assert user.phone == "11191919"


@pytest.mark.django_db
def test_create_test():

    order_test = 1

    assert order_test == 1