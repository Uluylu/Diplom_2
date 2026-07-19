import allure
import pytest
from api.user_client import UserClient
from api.order_client import OrderClient
from data.messages import ResponseMessages


class TestCreateOrder:

    @allure.title("Успешное создание заказа авторизованным пользователем")
    def test_order_create_by_authorized_user_success(self, created_user, available_ingredients):
        order = OrderClient()

        token = created_user["token"]
        payload = {"ingredients": available_ingredients}

        response = order.create_order(payload, token)

        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Создание заказа неавторизованным пользователем")
    def test_order_create_by_unauthorized_user(self, available_ingredients):
        order = OrderClient()

        payload = {"ingredients": available_ingredients}

        response = order.create_order(payload)

        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Попытка создания заказа с пустым списком ингредиентов")
    def test_order_create_missing_ingredients_error(self, created_user):
        order = OrderClient()

        token = created_user["token"]
        payload = {"ingredients": []}

        response = order.create_order(payload, token)

        assert response.status_code == 400
        assert response.json()["success"] is False
        assert response.json()["message"] == ResponseMessages.MISSING_INGREDIENTS

    @allure.title("Попытка создания заказа с несуществующим хешем ингредиента")
    def test_order_create_with_invalid_ingredient_hash_error(self, created_user):
        order = OrderClient()

        token = created_user["token"]
        payload = {"ingredients": ["wrong_hashe_123"]}

        response = order.create_order(payload, token)

        assert response.status_code == 500
