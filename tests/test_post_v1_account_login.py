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
    mailhog = MailhogApi(host='http://5.63.153.31:5025')
    api = Facade(host="http://5.63.153.31:5051")
    login = "as_29"
    email = "as_29@mail.ru"
    password = "password_29"
    json = Registration(
        login=login,
        email=email,
        password=password
    )
    response = api.account_api.post_v1_account(json=json)
    token = mailhog.get_token_from_last_email()
    response = api.account_api.put_v1_account_token(token=token)
    json = LoginCredentials(
        login=login,
        password=password,
        rememberMe=True
    )
    response = api.login_api.post_v1_account_login(json=json)

    assert_that(response.resource, has_properties(
        {
            "login": login,
            "roles": [UserRole.guest, UserRole.player],
            'medium_picture_url': None
        }
    ))
