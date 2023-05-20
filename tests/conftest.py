import pytest

from page_object.login.LoginPageObject import LoginPageObject


@pytest.fixture()
def open_login():
    login_page = LoginPageObject()
    yield login_page
    #login_page.close()
