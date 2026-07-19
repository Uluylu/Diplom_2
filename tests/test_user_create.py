import allure
import pytest
from api.user_client import UserClient
from data.messages import ResponseMessages
from helpers.helpers import generate_random_string


class TestCreateUser:

    @allure.title("Успешное создание пользователя со всеми обязательными полями")
    def test_user_create_success(self, user_cleanup):
        client = UserClient()
        
        email = f"{generate_random_string(10)}@yandex.ru"
        password = generate_random_string(10)
        name = generate_random_string(10)

        response = client.register_user(email, password, name)

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "accessToken" in response.json()

        token = response.json().get("accessToken")
        user_cleanup.append(token)

    @allure.title("Попытка создания уже созданного пользователя")
    def test_user_create_with_duplicate_email_error(self, created_user):
        client = UserClient()

        email = created_user["email"]
        password = created_user["password"]
        name = created_user["name"]
        response = client.register_user(email, password, name)

        assert response.status_code == 403
        assert response.json()["success"] is False
        assert response.json()["message"] == ResponseMessages.USER_ALREADY_EXISTS

    @allure.title("Попытка создания пользователя без одного из обязательных полей")
    @pytest.mark.parametrize("missing_field", ["email", "password", "name"])
    def test_user_create_with_missing_required_field_error(self, missing_field):
        client = UserClient()

        user_data = {
            "email": f"{generate_random_string(10)}@yandex.ru",
            "password": generate_random_string(10),
            "name": generate_random_string(10)
        }

        user_data[missing_field] = ""

        response = client.register_user(
            email = user_data["email"], 
            password = user_data["password"], 
            name = user_data["name"]
        )

        assert response.status_code == 403
        assert response.json()["success"] is False
        assert response.json()["message"] == ResponseMessages.MISSING_REQUIRED_FIELDS
