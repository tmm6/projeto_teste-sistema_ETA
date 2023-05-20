import pytest
from page_object.login.LoginPageObject import LoginPageObject


# Fixture para realizar o login
@pytest.fixture()
def login_page():
    login_page = LoginPageObject()
    yield login_page
    login_page.close()


@pytest.fixture()
def login(login_page):
    login_page.login()
    yield login_page

