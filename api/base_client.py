from data.urls import Urls


class BaseClient:
    def __init__(self):
        self.base_url = Urls.BASE_URL
        self.headers = {"Content-Type": "application/json"}