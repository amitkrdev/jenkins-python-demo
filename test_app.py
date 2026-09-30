import os
import pytest
from app import login

def test_credentials_are_present():
    assert os.environ.get("APP_USER"), "APP_USER is missing"
    assert os.environ.get("APP_PASS"), "APP_PASS is missing"

def test_login_works():
    assert login() is True