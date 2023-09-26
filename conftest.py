import pytest
from generic.helpers.mailhog import MailhogApi
from generic.helpers.dm_db import DmDatabase
from services.dm_api_account import Facade
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


@pytest.fixture()
def mailhog():
    return MailhogApi(host='http://5.63.153.31:5025')


@pytest.fixture()
def dm_api_facade(mailhog):
    return Facade(host="http://5.63.153.31:5051", mailhog=mailhog)


@pytest.fixture()
def dm_db():
    db = DmDatabase(user='postgres', password='admin', host='5.63.153.31', database='dm3.5')
    return db
