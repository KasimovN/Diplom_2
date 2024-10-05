import pytest
from data import ApiData
from helper import Helper
from starburger_api import StarburgerApi


class TestLogin:
    def test_login_success(self):
        body = Helper.create_fake_registration_body()
        new_user = StarburgerApi.user_registration(body)
        new_user_token = new_user.json()['accessToken']
        del body['name']
        login_response = StarburgerApi.login(body)
        deleted_user = StarburgerApi.delete_user(new_user_token)
        assert (login_response.status_code == 200
                and new_user.json()['user']['email'] == login_response.json()['user']['email'])

    @pytest.mark.parametrize('param', ApiData.REQUIRED_LOGIN_PARAM)
    def test_login_fail_creds(self, param):
        body = Helper.create_fake_registration_body()
        new_user = StarburgerApi.user_registration(body)
        new_user_token = new_user.json()['accessToken']
        del body['name']
        body[param] = body[param] + '123'
        login_response = StarburgerApi.login(body)
        login_massage = login_response.json()['message']
        deleted_user = StarburgerApi.delete_user(new_user_token)
        assert login_response.status_code == 401 and login_massage == ApiData.RESPONSE_BODY_ERROR_LOGIN
