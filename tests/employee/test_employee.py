import time

from page_object.employee.EmployeePageObject import EmployeePageObject
from page_object.menu.MenuPageObject import MenuPageObject


class Test_Employee:
    def test_add_employee_without_photo(self, login):
        """
        1- No menu, clique na opção "PIM" OK
        2- Clique no botão "+ Add"
        3- Preencha os campos "Employee Full Name" e "Employee Id".
        4- Clicar no botão "Save"
        :param login:
        :return:
        """
        menu = MenuPageObject(driver=login.driver)
        assert menu.pim_option_menu(), 'Página diferente'

        employee = EmployeePageObject(driver=menu.driver)
        employee.add_employee()
        # assert employee.add_employee(), 'Página diferente'
        #time.sleep(3)
