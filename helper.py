from faker import Faker
from data import ApiData


class Helper:
    @staticmethod
    def create_fake_registration_body():
        body = ApiData.BODY_USER_REGISTRATION.copy()
        fake = Faker()
        body['email'] = fake.email()
        body['password'] = fake.password()
        body['name'] = fake.name()

        return body

    @staticmethod
    def body_change_creds():
        random_body = Helper.create_fake_registration_body()
        body = []
        for i in ApiData.REQUIRED_REGISTER_PARAM:
            param = {i: random_body[i]}
            body.append(param)
        return body
