import time
from generic.helpers.mailhog import MailhogApi

def test_post_v1_account(dm_api_facade, dm_db):
    mailhog = MailhogApi(host='http://5.63.153.31:5025')
    login = "as_1012"
    email = "as_1012@mail.ru"
    password = "password_1012"
    dm_db.delete_user_by_login(login=login)
    dataset = dm_db.get_user_by_login(login=login)
    assert len(dataset) == 0

    response = dm_api_facade.account.register_new_user(
        login=login,
        email=email,
        password=password
    )
    dataset = dm_db.get_user_by_login(login=login)
    for row in dataset:
        assert row['Login'] == login, f'User {login} not registered'
        assert row['Activated'] is False, f'User {login} was activated'

    dataset = dm_db.activate_user_by_login(login=login)

    time.sleep(2)
    dataset = dm_db.get_user_by_login(login=login)
    for row in dataset:
        assert row['Activated'] is True, f'User {login} not activated'

    dm_api_facade.login.login_user(
        login=login,
        password=password
    )
