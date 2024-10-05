import pytest
from data import ApiData
from helper import Helper
from starburger_api import StarburgerApi


class TestChangeUserCreds:
    @pytest.mark.parametrize('change_cred', Helper.body_change_creds())
    def test_change_user_creds_success(self, change_cred, create_user):
        token = create_user.json()['accessToken']
        change_response = StarburgerApi.change_user_creds(token, change_cred)
        assert change_response.status_code == 200 and change_response.json()['success']

    @pytest.mark.parametrize('change_cred', Helper.body_change_creds())
    def test_change_user_creds_without_token(self, change_cred, create_user):
        token = ''
        change_response = StarburgerApi.change_user_creds(token, change_cred)
        assert (change_response.status_code == 401 and change_response.json()['message'] ==
                ApiData.ERROR_AUTHORIZATION_BODY)
