import requests
import random
import string
from data.urls import Urls


def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

def generate_random_user():
    email_list = ["gmail.com", "yandex.ru", "ya.ru", "mail.ru", "inbox.ru"]
    names_list = ["Иван", "Алексей", "Мария", "Дмитрий", "Елена", "Сергей", "Ольга"]
    random_email = f"Test_login{random.randint(100,999)}@{random.choice(email_list)}"
    random_valid_password = f"{random.randint(100000,999999)}"
    random_name = f"{random.choice(names_list)}{random.randint(100,999)}"

    return {
        "email": random_email,
        "password": random_valid_password,
        "name": random_name
        }

def register_new_user_and_return_email_password():

    login_pass = []

    email_list = ["gmail.com", "yandex.ru", "ya.ru", "mail.ru", "inbox.ru"]
    email = f"{generate_random_string(10)}@{random.choice(email_list)}"
    password = generate_random_string(10)
    name = generate_random_string(10)

    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    response = requests.post(Urls.CREATE_USER, json=payload)

    if response.status_code == 200:
        login_pass.append(email)
        login_pass.append(password)
        login_pass.append(name)
        token = response.json().get("accessToken")
        login_pass.append(token)

    return login_pass
