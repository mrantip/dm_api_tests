import structlog

from dm_api_account.models import ChangePassword
from services.dm_api_account import Facade

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_password():
    api = Facade(host="http://5.63.153.31:5051")
    login = "as_108"
    email = "as_108@mail.ru"
    password = "password_108"
    oldPassword = password
    newPassword = "1password_108"

    response = api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )
    api.account.activate_registered_user(login=login)
    api.login.login_user(
        login=login,
        password=password
    )

    api.account.reset_registered_user_password(login=login, email=email)
    token = api.mailhog.get_token_for_reset_password(login=login)
    api.account.change_registered_user_password(login=login, token=token, old_password=oldPassword, new_password=newPassword)

    # api.account.set_headers(headers=token)
    # api.login.set_headers(headers=token)

    # json = ChangePassword(
    #     login=login,
    #     token='91aca3a4-e521-44fd-961e-702cb9ea8639',
    #     old_password=password,
    #     new_password="1password_1"
    # )
    # response = api.account_api.put_v1_account_password(json=json)
