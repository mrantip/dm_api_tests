from services.dm_api_account import Facade
import structlog

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
