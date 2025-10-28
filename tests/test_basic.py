from importlib.metadata import version

import pytest

from src import hentailib


def test_import():
    assert hentailib is not None

def test_version():
    assert version("hentailib") is not None