import pytest
from page_object.login.LoginPageObject import LoginPageObject


# Fixture para realizar o login
@pytest.fixture()
def open_login():
    login_page = LoginPageObject()
    yield login_page
    login_page.close()
