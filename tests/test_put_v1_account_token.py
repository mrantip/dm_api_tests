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
    mailhog = MailhogApi(host='http://5.63.153.31:5025')
    api = Facade(host="http://5.63.153.31:5051")
    login = "as_27"
    email = "as_27@mail.ru"
    password = "password_27"
    json = Registration(
        login=login,
        email=email,
        password=password
    )
    response = api.account_api.post_v1_account(json=json)
    token = mailhog.get_token_from_last_email()
    response = api.account_api.put_v1_account_token(token=token)
    assert_that(response.resource, has_properties(
        {
            "login": login,
            "roles": [UserRole.guest, UserRole.player]
        }
    ))
