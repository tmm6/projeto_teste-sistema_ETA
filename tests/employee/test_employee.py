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
        assert employee.access_add_employee_page(), 'Página diferente'
        employee.add_employee()
        #time.sleep(5)
        #assert employee.add_employee(), 'Toast não é exibido'
        assert employee.verify_employee_info(), 'Nome diferente'
        time.sleep(3)

        # Ao final do teste excluir o cadastro