import pytest
from authentification.models import UpiUser




@pytest.fixture
def user(db):
    user = UpiUser(phone="111919192", password="test@123")
    user.is_staff=True
    user.save()
    print("=====> ", user.is_active)
    return user

@pytest.fixture
def order_test():
    return 1