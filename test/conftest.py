import pytest
from authentification.models import UpiUser




@pytest.fixture
def user():
    user_dc = UpiUser(phone="111919191", password="liverpool")
    user = user.save()
    print("======>", user.password)
    return user

@pytest.fixture
def order_test():
    return 1