import requests


def delete_v1_account_login_all():
    """
    Logout from every device
    :return:
    """
    url = "http://5.63.153.31:5051/v1/account/login/all"

    headers = {
        'X-Dm-Auth-Token': 'aliquip labore in ipsum',
        'X-Dm-Bb-Render-Mode': 'aliquip labore in ipsum',
        'Accept': 'text/plain'
    }

    response = requests.request(
        method="DELETE",
        url=url,
        headers=headers
    )

    return response
