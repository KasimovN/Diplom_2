import requests

from data import ApiData
from helper import Helper


class StarburgerApi:
    @staticmethod
    def user_registration(body):
        registration_response = requests.post(ApiData.URL + ApiData.USER_REGISTRATION_API, json=body)
        return registration_response

    @staticmethod
    def delete_user(accesstoken):
        delete_response = requests.delete(ApiData.URL + ApiData.USER_API, headers={'Authorization': accesstoken})
        return delete_response


responce = StarburgerApi.user_registration(Helper.create_fake_registration_body())
print(responce.status_code)
deleted = StarburgerApi.delete_user(responce.json()['accessToken'])
print(deleted.status_code)
