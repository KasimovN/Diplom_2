import requests

from data import ApiData
# from helper import Helper


class StarburgerApi:
    @staticmethod
    def user_registration(body):
        registration_response = requests.post(ApiData.URL + ApiData.USER_REGISTRATION_API, json=body)
        return registration_response

    @staticmethod
    def delete_user(accesstoken):
        delete_response = requests.delete(ApiData.URL + ApiData.USER_API, headers={'Authorization': accesstoken})
        return delete_response

    @staticmethod
    def login(body):
        login_response = requests.post(ApiData.URL + ApiData.USER_LOGIN_API, json=body)
        return login_response

    @staticmethod
    def change_user_creds(accesstoken, body):
        change_response = requests.patch(ApiData.URL + ApiData.USER_API, json=body,
                                         headers={'Authorization': accesstoken})
        return change_response
token = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY2ZjZmZmY1OWVkMjgwMDAxYjRjNDkwZSIsImlhdCI6MTcyNzUxNzM0NywiZXhwIjoxNzI3NTE4NTQ3fQ.846D9VgsukSrBbGcCHY4O_nbjydD2z-pT3gFP4O96y8'
body = {"name": "NikolaiKasimov777"}
print(StarburgerApi.change_user_creds(token,body).json())