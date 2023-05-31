import time

from page_object.employee.EmployeePageObject import EmployeePageObject
from page_object.menu.MenuPageObject import MenuPageObject


class Test_Employee:
    def test_add_employee_without_photo(self, after_tests_employee):
        """
        1- No menu, clique na opção "PIM"
        2- Clique no botão "+ Add" OK
        3- Preencha os campos "Employee Full Name".
        4- Clicar no botão "Save". OK
        5- Verificar se o toast aparece.
        6- Verificar se vai pra tela de editar funcionario.
        6.1- Verificar o nome do funcionário.
        6.2-Verificar o título da página.

        Após o teste
        1- Realizar uma busca pelo funcionário recém cadastrado
        2- Excluir funcionário
        """
        menu = MenuPageObject(driver=after_tests_employee.driver)
        assert menu.pim_option_menu(), 'Página diferente'

        employee = EmployeePageObject(driver=menu.driver)
        assert employee.access_add_employee_page(), 'Página diferente'
        assert employee.add_employee(), 'Toast não é exibido'
        assert employee.verify_employee_name(), 'Nome diferente'
        #assert employee.verify_employee_profile_titles(), 'Página diferente do perfil'
        time.sleep(3)

        # Ao final do teste excluir o cadastro

    def test_search_employee_by_name(self, login):
        menu = MenuPageObject(driver=login.driver)
        assert menu.pim_option_menu(), 'Página diferente'
        employee = EmployeePageObject(driver=menu.driver)
        employee.search_employee()
        time.sleep(5)

    def test_delete_employee(self, login):
        menu = MenuPageObject(driver=login.driver)
        assert menu.pim_option_menu(), 'Página diferente'
        employee = EmployeePageObject(driver=menu.driver)
        employee.delete_employee()
