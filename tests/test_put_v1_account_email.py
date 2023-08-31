from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi
import structlog
from dm_api_account.models.registration_model import Registration
from dm_api_account.models.change_email_model import ChangeEmail
from hamcrest import assert_that, has_properties
from dm_api_account.models.user_envelope_model import UserRole, Rating
import json

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_email():
    mailhog = MailhogApi(host='http://5.63.153.31:5025')
    api = DmApiAccount(host="http://5.63.153.31:5051")
    login = "as_30"
    email = "as_30@mail.ru"
    password = "password_30"
    email_new = "as1_30@mail.ru"
    json = Registration(
        login=login,
        email=email,
        password=password
    )
    response = api.account.post_v1_account(json=json)
    token = mailhog.get_token_from_last_email()
    response = api.account.put_v1_account_token(token=token)
    json = ChangeEmail(
        login=login,
        password=password,
        email=email_new
    )
    response = api.account.put_v1_account_email(json=json)

    assert_that(response.resource, has_properties(
        {
            "login": login,
            "roles": [UserRole.guest, UserRole.player],
            'status': None
        }
    ))
