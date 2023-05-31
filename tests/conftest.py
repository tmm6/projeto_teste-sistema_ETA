import pytest

from page_object.employee.EmployeePageObject import EmployeePageObject
from page_object.login.LoginPageObject import LoginPageObject
from page_object.menu.MenuPageObject import MenuPageObject


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

@pytest.fixture()
def after_tests_employee(login):
    menu = MenuPageObject(driver=login.driver)
    employee = EmployeePageObject(driver=menu.driver)
    yield login
    menu.pim_option_menu()
    employee.delete_employee()
