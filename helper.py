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
