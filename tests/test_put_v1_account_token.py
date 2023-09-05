from services.dm_api_account import Facade
from dm_api_account.generic.helpers.mailhog import MailhogApi
import structlog
from dm_api_account.models.registration_model import Registration
from hamcrest import assert_that, has_properties
from dm_api_account.models.user_envelope_model import UserRole

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_token():
    api = Facade(host="http://5.63.153.31:5051")
    login = "as_3"
    email = "as_3@mail.ru"
    password = "password_3"

    response = api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )
    api.account.activate_registered_user(login=login)

    # assert_that(response.resource, has_properties(
    #     {
    #         "login": login,
    #         "roles": [UserRole.guest, UserRole.player]
    #     }
    # ))
