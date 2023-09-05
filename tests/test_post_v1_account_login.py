from services.dm_api_account import Facade
from dm_api_account.generic.helpers.mailhog import MailhogApi
import structlog
from dm_api_account.models.registration_model import Registration
from dm_api_account.models.login_credentials_model import LoginCredentials
from hamcrest import assert_that, has_properties
from dm_api_account.models.user_envelope_model import UserRole

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account_login():
    api = Facade(host="http://5.63.153.31:5051")
    api.login.login_user(login="as_40", password="password_40", remember_me=True)

    login = "as_29"
    email = "as_29@mail.ru"
    password = "password_29"
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

    # assert_that(response.resource, has_properties(
    #     {
    #         "login": login,
    #         "roles": [UserRole.guest, UserRole.player],
    #         'medium_picture_url': None
    #     }
    # ))
