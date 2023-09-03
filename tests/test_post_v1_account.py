from services.dm_api_account import Facade
import structlog
from hamcrest import assert_that, has_properties

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account():
    api = Facade(host="http://5.63.153.31:5051")
    login = "as_47"
    email = "as_47@mail.ru"
    password = "password_47"

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
    #         "rating": Rating(enabled=True, quality=0, quantity=0)
    #     }
    # ))
