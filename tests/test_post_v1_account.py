import time

from generic.helpers.dm_db import DmDatabase
from services.dm_api_account import Facade
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account():
    api = Facade(host="http://5.63.153.31:5051")
    login = "as_106"
    email = "as_106@mail.ru"
    password = "password_106"
    db = DmDatabase(user='postgres', password='admin', host='5.63.153.31', database='dm3.5')
    db.delete_user_by_login(login=login)
    dataset = db.get_user_by_login(login=login)
    assert len(dataset) == 0

    response = api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )
    dataset = db.get_user_by_login(login=login)
    for row in dataset:
        assert row['Login'] == login, f'User {login} not registered'
        assert row['Activated'] is False, f'User {login} was activated'

    dataset = db.activate_user_by_login(login=login)
    # api.account.activate_registered_user(login=login)
    time.sleep(2)
    dataset = db.get_user_by_login(login=login)
    for row in dataset:
        assert row['Activated'] is True, f'User {login} not activated'

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
