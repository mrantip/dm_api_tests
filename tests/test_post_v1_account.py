import requests
from services.dm_api_account import DmApiAccount


def test_post_v1_account():
    api = DmApiAccount(host="http://5.63.153.31:5051")
    json = {
        "login": "login_16",
        "email": "login_16@mail.ru",
        "password": "login_16"
    }
    response = api.account.post_v1_account(
        json=json
    )
    print(response)
