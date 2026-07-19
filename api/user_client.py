import requests
import allure
from data.urls import Urls
from api.base_client import BaseClient

class UserClient(BaseClient):

    @allure.step("Регистрация нового пользователя")
    def register_user(self, email, password, name):
        body = {
            "email": email,
            "password": password,
            "name": name
        }
        
        return requests.post(Urls.CREATE_USER, json=body, headers=self.headers)
    
    @allure.step("Вход пользователя в систему")
    def login_user(self, email, password):
        body = {
            "email": email,
            "password": password
        }
        
        return requests.post(Urls.LOGIN_USER, json=body, headers=self.headers)
    
    @allure.step("Удаление пользователя по токену")
    def delete_user(self, token):
        headers = {"Authorization": token}
        
        return requests.delete(Urls.USER_DATA, headers=headers)
    