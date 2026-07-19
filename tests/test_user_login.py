import allure
import pytest
from api.user_client import UserClient
from data.messages import ResponseMessages
from helpers.helpers import generate_random_string


class TestLoginUser:
    
    @allure.title("Успешная авторизация пользователя под существующими данными")
    def test_user_login_success(self, created_user):
        client = UserClient()

        email = created_user["email"]
        password = created_user["password"]

        response = client.login_user(email, password)

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "accessToken" in response.json()

    @allure.title("Ошибка авторизации при вводе неверного логина или пароля")
    @pytest.mark.parametrize("incorrect_field, wrong_value",
                            [
                                ("email", f"{generate_random_string(10)}@yandex.ru"),
                                ("password", generate_random_string(10))
                            ])
    def test_user_login_with_incorrect_credentials_error(self, incorrect_field, wrong_value, created_user):
        client = UserClient()

        user_data = {
            "email":created_user["email"],
            "password":created_user["password"]

        }

        user_data[incorrect_field] = wrong_value

        response = client.login_user(
            email = user_data["email"],
            password = user_data["password"])

        assert response.status_code == 401
        assert response.json()["success"] is False
        assert response.json()["message"] == ResponseMessages.INCORRECT_CREDENTIALS
        
