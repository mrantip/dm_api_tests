import requests


def post_v1_account_password():
    """
    Reset registered user password
    :return:
    """
    url = "http://5.63.153.31:5051/v1/account/password"

    payload = {
        "login": "et aliquip esse",
        "email": "culpa Excepteur"
    }
    headers = {
        'X-Dm-Auth-Token': 'aliquip labore in ipsum',
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
