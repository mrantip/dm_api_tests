import requests
from services.dm_api_account import DmApiAccount

def test_put_v1_account_token():
    api = DmApiAccount(host="http://5.63.153.31:5051")
    token = "1fshad23324345fdhsfdhsf"
    response = api.account.put_v1_account_token(
        token=token
    )
    print(response)
