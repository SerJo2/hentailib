import os
import pytest

from dotenv import load_dotenv

from src.hentailib import Rule34Api

load_dotenv()

@pytest.fixture
def api_key():
    key = os.getenv("HENTAILIB_API_KEY")
    if not key:
        pytest.skip("Key is not set up")
    return key

@pytest.fixture
def user_id():
    user_id = os.getenv("HENTAILIB_USER_ID")
    if not user_id:
        pytest.skip("User_id is not set up")
    return user_id

@pytest.fixture
def api_client(api_key, user_id):
    return Rule34Api(api_key, user_id)

