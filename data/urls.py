class Urls:

    BASE_URL = 'https://stellarburgers.education-services.ru'

    CREATE_USER = f"{BASE_URL}/api/auth/register"
    LOGIN_USER = f"{BASE_URL}/api/auth/login"
    USER_DATA = f"{BASE_URL}/api/auth/user"
    LOGOUT_USER = f"{BASE_URL}/api/auth/logout"
    
    INGREDIENTS = f"{BASE_URL}/api/ingredients"
    ORDERS = f"{BASE_URL}/api/orders"