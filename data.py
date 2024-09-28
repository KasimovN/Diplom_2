

class ApiData:
    URL = 'https://stellarburgers.nomoreparties.site/'
    USER_REGISTRATION_API = 'api/auth/register'
    USER_API = 'api/auth/user'
    USER_LOGIN_API = 'api/auth/login'
    BODY_USER_REGISTRATION = {
            "email": "kasimov.nn@yandex.ru3",
            "password": "password",
            "name": "NikolaiKasimov3"
        }
    REQUIRED_REGISTER_PARAM = ["email", "password", "name"]
    RESPONSE_BODY_ERROR_REGISTRATION = 'Email, password and name are required fields'
    RESPONSE_BODY_ERROR_LOGIN = "email or password are incorrect"
    REQUIRED_LOGIN_PARAM = ["email", "password"]
