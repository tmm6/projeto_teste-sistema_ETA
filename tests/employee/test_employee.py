import time

from page_object.employee.EmployeePageObject import EmployeePageObject
from page_object.menu.MenuPageObject import MenuPageObject


class Test_Employee:
    def test_add_employee_without_photo(self, after_add_tests_employee):
        menu = MenuPageObject(driver=after_add_tests_employee.driver)
        assert menu.pim_option_menu(), 'Página diferente'

        employee = EmployeePageObject(driver=menu.driver)
        assert employee.access_add_employee_page(), 'Página diferente'
        assert employee.add_employee(), 'Cadastro não realizado'
        assert employee.verify_employee_name(), 'Nome diferente'
        assert employee.verify_employee_profile_titles(), 'Página diferente do perfil'
        time.sleep(3)

    def test_search_employee_by_name(self, before_after_search_tests_employee):
        menu = MenuPageObject(driver=before_after_search_tests_employee.driver)
        assert menu.pim_option_menu(), 'Página diferente'
        employee = EmployeePageObject(driver=menu.driver)
        employee.search_employee()
        employee.verify_search_result()
        time.sleep(5)

    def test_delete_employee(self, before_delete_tests_employee):
        menu = MenuPageObject(driver=before_delete_tests_employee.driver)
        assert menu.pim_option_menu(), 'Página diferente'
        employee = EmployeePageObject(driver=menu.driver)
        employee.search_employee()
        assert employee.delete_employee(), 'Exclusão não realizada'
        employee.search_employee()
        assert employee.verify_search_result(), 'Funcionário ainda existe'

    def test_algo(self, login):
        menu = MenuPageObject(driver=login.driver)
        menu.pim_option_menu()
        employee = EmployeePageObject(driver=menu.driver)

        assert employee.verify_employee_profile_titles(), 'Putz, deu ruim'

