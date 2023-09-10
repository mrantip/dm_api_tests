from dm_api_account.apis.account_api import AccountApi
from dm_api_account.apis.login_api import LoginApi
from generic.helpers.login import Login
from generic.helpers.mailhog import MailhogApi
from generic.helpers.account import Account


class Facade:
    def __init__(self, host: object, mailhog_host: object = None, headers: object = None) -> object:
        self.account_api = AccountApi(host, headers)
        self.login_api = LoginApi(host, headers)
        self.mailhog = MailhogApi()
        self.account = Account(self)
        self.login = Login(self)
