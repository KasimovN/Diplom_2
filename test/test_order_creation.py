from data import ApiData
from starburger_api import StarburgerApi


class TestOrder:

    def test_create_order_with_ingredients_success(self, create_user):
        token = create_user.json()['accessToken']
        order_response = StarburgerApi.create_order(token, ApiData.DODY_CREATE_ORDER)
        assert order_response.status_code == 200 and ApiData.DODY_CREATE_ORDER["ingredients"][0] in order_response.text

    def test_create_order_without_ingredients(self, create_user):
        token = create_user.json()['accessToken']
        order_response = StarburgerApi.create_order(token, [])
        assert (order_response.status_code == 400
                and order_response.json()['message'] == 'Ingredient ids must be provided')

    def test_create_order_with_wrong_ingredients(self, create_user):
        token = create_user.json()['accessToken']
        order_response = StarburgerApi.create_order(token, ApiData.DODY_CREATE_ORDER_WRONG)
        assert order_response.status_code == 500

    def test_create_order_without_authorization(self):
        order_response = StarburgerApi.create_order('' , ApiData.DODY_CREATE_ORDER)
        assert (order_response.status_code == 200
                and ApiData.DODY_CREATE_ORDER["ingredients"][0] not in order_response.text)
