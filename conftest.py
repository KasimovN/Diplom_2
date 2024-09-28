import pytest

from data import ApiData
from helper import Helper
from starburger_api import StarburgerApi


@pytest.fixture()
def create_user():
    created_user = StarburgerApi.user_registration(Helper.create_fake_registration_body())
    token = created_user.json()['accessToken']

    yield created_user

    StarburgerApi.delete_user(token)


@pytest.fixture()
def create_order(create_user):
    created_order = StarburgerApi.create_order(create_user.json()['accessToken'], ApiData.DODY_CREATE_ORDER)
    return [created_order, create_user.json()['accessToken']]
