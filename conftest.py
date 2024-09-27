import pytest

from helper import Helper
from starburger_api import StarburgerApi


@pytest.fixture()
def create_user():
    created_user = StarburgerApi.user_registration(Helper.create_fake_registration_body())
    token = created_user.json()['accessToken']

    yield created_user

    StarburgerApi.delete_user(token)
