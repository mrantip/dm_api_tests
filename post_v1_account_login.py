import requests


def post_v1_account_login():
    """
    Authenticate via credentials
    :return:
    """
    url = "http://5.63.153.31:5051/v1/account/login"

    payload = {
        "login": "culpa labor",
        "password": "mollit tempor",
        "rememberMe": True
    }
    headers = {
        'X-Dm-Bb-Render-Mode': 'aliquip labore in ipsum',
        'Content-Type': 'application/json',
        'Accept': 'text/plain'
    }

    response = requests.request(
        method="POST",
        url=url,
        headers=headers,
        json=payload
    )

    return response
