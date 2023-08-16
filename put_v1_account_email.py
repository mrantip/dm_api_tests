import requests


def put_v1_account_email():
    """
    Change registered user email
    :return:
    """
    url = "http://5.63.153.31:5051/v1/account/email"

    payload = {
        "login": "eu dolor veniam labore",
        "password": "ut consequat dolore dolore",
        "email": "fugiat consequat aute"
    }
    headers = {
        'X-Dm-Auth-Token': 'aliquip labore in ipsum',
        'X-Dm-Bb-Render-Mode': 'aliquip labore in ipsum',
        'Content-Type': 'application/json',
        'Accept': 'text/plain'
    }

    response = requests.request(
        method="PUT",
        url=url,
        headers=headers,
        json=payload
    )

    return response
