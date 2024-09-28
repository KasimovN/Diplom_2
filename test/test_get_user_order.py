from starburger_api import StarburgerApi


class TestGetUserOrder:
    def test_get_user_order_succsess(self, create_order):
        token = create_order[1]
        created_order_number = str(create_order[0].json()['order']['number'])
        get_order = StarburgerApi.get_order(token)
        assert get_order.status_code == 200 and created_order_number in get_order.text

    def test_get_user_order_without_authorization(self):
        get_order = StarburgerApi.get_order('')
        assert get_order.status_code == 401 and get_order.json()['message'] == "You should be authorised"
