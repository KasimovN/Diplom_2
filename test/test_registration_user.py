from helper import Helper
from starburger_api import StarburgerApi


class TestRegistrationUser:
    def test_create_user_succsess(self, create_user):
        status_code = create_user.status_code
        body = create_user.json()
        assert status_code == 200 and len(body) == 4 and body['user']

    def test_create_user_dublicate(self):
        body = Helper.create_fake_registration_body()

        new_user = StarburgerApi.user_registration(body)
        new_user_token = new_user.json()['accessToken']

        duplicate_user = StarburgerApi.user_registration(body)

        deleted_new_user = StarburgerApi.delete_user(new_user_token)

        assert (duplicate_user.status_code == 403 and duplicate_user.json()['message'] == 'User already exists'
                and deleted_new_user.status_code == 202)
