def test_get_v1_account(dm_api_facade):
    login = "as_106"
    email = "as_106@mail.ru"
    password = "password_106"

    token = dm_api_facade.login.get_auth_token(login=login, password=password)
    dm_api_facade.account.set_headers(headers=token)
    dm_api_facade.login.set_headers(headers=token)
    dm_api_facade.account.get_current_user_info()
    dm_api_facade.login.logout_user()
