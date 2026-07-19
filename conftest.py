import pytest
from helpers.helpers import register_new_user_and_return_email_password
from api.user_client import UserClient
from api.order_client import OrderClient


@pytest.fixture
def created_user():
    client = UserClient()
    
    email, password, name, token = register_new_user_and_return_email_password()
    
    yield {"email": email, "password": password, "name": name, "token": token}
    
    if token:
        client.delete_user(token)

@pytest.fixture
def user_cleanup():
    tokens_to_delete = []
    
    yield tokens_to_delete
    
    client = UserClient()
    for token in tokens_to_delete:
        if token:
            client.delete_user(token)

@pytest.fixture
def available_ingredients():
    client = OrderClient()
    
    response = client.get_ingredients()
    ingredients_data = response.json()["data"]
    
    hash_1 = ingredients_data[0]["_id"]
    hash_2 = ingredients_data[1]["_id"]
    
    return [hash_1, hash_2]
