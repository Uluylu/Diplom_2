import requests
import allure
from data.urls import Urls
from api.base_client import BaseClient

class OrderClient(BaseClient):
    
    @allure.step("Получаем список ингредиентов")
    def get_ingredients(self):
        return requests.get(Urls.INGREDIENTS, headers=self.headers)

    @allure.step("Создание нового заказа")
    def create_order(self, ingredients_payload, token=None):
        if token:
            headers = {
                "Content-Type": "application/json",
                "Authorization": token
            }
        
            return requests.post(Urls.ORDERS, json=ingredients_payload, headers=headers)
    
        return requests.post(Urls.ORDERS, json=ingredients_payload, headers=self.headers)
    