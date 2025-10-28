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
def api_client(api_key):
    return Rule34Api(api_key)

