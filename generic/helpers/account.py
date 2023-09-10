from uuid import UUID

from pydantic import StrictStr

from dm_api_account.models import Registration, ChangePassword, ResetPassword


class Account:
    def __init__(self, facade):
        self.facade = facade

    def set_headers(self, headers):
        self.facade.account_api.client.session.headers.update(headers)

    def register_new_user(self, login: str, email: str, password: str):
        response = self.facade.account_api.post_v1_account(
            json=Registration(
                login=login,
                email=email,
                password=password
            )
        )
        return response

    def activate_registered_user(self, login: str):
        token = self.facade.mailhog.get_token_by_login(login=login)
        response = self.facade.account_api.put_v1_account_token(
            token=token
        )
        return response

    def get_current_user_info(self, **kwargs):
        response = self.facade.account_api.get_v1_account(**kwargs)
        return response

    def reset_registered_user_password(self, login: str, email: str):
        response = self.facade.account_api.post_v1_account_password(
            json=ResetPassword(
                login=login,
                email=email,
            )
        )
        return response

    def change_registered_user_password(self, login: str, token: str, old_password: str, new_password: str):
        # token = self.facade.mailhog.get_token_for_reset_password(login=login)
        response = self.facade.account_api.put_v1_account_password(
            json=ChangePassword(
                login=login,
                token=token,
                old_password=old_password,
                new_password=new_password
            )
        )
        return response
