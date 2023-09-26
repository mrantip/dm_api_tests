from hamcrest import assert_that, has_properties

from dm_api_account.models.user_envelope_model import UserRole
from services.dm_api_account import Facade
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_token():
    api = Facade(host="http://5.63.153.31:5051")
    login = "as_111"
    email = "as_111@mail.ru"
    password = "password_111"

    response = api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )
    api.account.activate_registered_user(login=login)

    assert_that(response.resourse, has_properties(
        {
            "login": login,
            "roles": [UserRole.guest, UserRole.player]
        }
    ))
