import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from page_object.PageObject import PageObject
from selenium.webdriver.support import expected_conditions as EC


class EmployeePageObject(PageObject):
    # Locators
    ## URLs
    url_add_employee = 'https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee'

    ## Elements
    css_name_first_name = 'firstName'
    css_name_middle_name = 'middleName'
    css_name_last_name = 'lastName'
    css_button_save = '[type="submit"]'
    css_class_toast = 'oxd-toast-container--toast'
    css_class_title_add_employee = 'orangehrm-main-title'
    css_class_name_employee = 'orangehrm-edit-employee-name'
    css_placeholder_employee_name = '[placeholder="Type for hints..."]'
    css_class_cells_employees = '[role = "cell"]'
    css_class_delete_employee_button = 'bi-trash'

    ## Text
    text_add_employee_button = 'Add'
    text_search_employee = 'Search'
    text_title_add_employee = 'Add Employee'
    text_first_name = 'Barbie'
    text_middle_name = 'Millicent'
    text_last_name = 'Roberts'
    text_toast_msg = 'Successfully Saved'

    def __init__(self, driver):
        super().__init__(driver=driver)

    # Métodos para preencher os campos
    def first_name_field(self):
        self.driver.find_element(By.NAME, self.css_name_first_name).send_keys(self.text_first_name)

    def middle_name_field(self):
        self.driver.find_element(By.NAME, self.css_name_middle_name).send_keys(self.text_middle_name)

    def last_name_field(self):
        self.driver.find_element(By.NAME, self.css_name_last_name).send_keys(self.text_last_name)

    def click_button_save_employee(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_button_save).click()

    # Método para acessar a tela de adicionar um funcionário.
    def access_add_employee_page(self):
        self.click_correct_button(expect_title=self.text_add_employee_button)
        return self.verify_title(self.text_title_add_employee, self.css_class_title_add_employee) and \
            self.verify_url(self.url_add_employee)

    def add_employee(self):
        """
        Método para adicionar um usuário. Ao final é verificado o toast.
        :return:
        """
        self.first_name_field()
        self.middle_name_field()
        self.last_name_field()
        self.click_button_save_employee()
        # Verificar se o toast de confirmação do cadastro é exibido
        toast = WebDriverWait(self.driver, timeout=5).until(
            lambda toast_element: toast_element.find_element(By.CLASS_NAME, self.css_class_toast))
        print(toast.text)
        result = self.text_toast_msg in toast.text
        print(result)
        return result

    def verify_employee_info(self):
        current_name = WebDriverWait(self.driver, timeout=10).until(
            lambda toast_element: toast_element.find_element(By.CLASS_NAME, self.css_class_name_employee))

        name = ' '.join([self.text_first_name, self.text_last_name])
        return name == current_name

    def search_employee(self):
        list_elements_search = self.driver.find_elements(By.CSS_SELECTOR, self.css_placeholder_employee_name)
        employee_name = list_elements_search[0]
        employee_name.send_keys('Charlie')
        self.click_correct_button(expect_title=self.text_search_employee)
        # Trocar por um WebDriverWait
        time.sleep(1)
        list_employees = self.driver.find_elements(By.CSS_SELECTOR, self.css_class_cells_employees)
        if list_employees[2].text == 'Charlie':
            return True

    def delete_employee(self):
        """
        1 - Pesquisar um funcionario
        2 - Verificar se ele está na lista
        3 - Clicar no ícone da lixeira
        4 - Clicar em confirmar no popup
        5 - Verificar toast
        6 - Verificar que tem 0 ocorrências na lista de funcionários
        """
        if self.search_employee():
            time.sleep(2)
            self.driver.find_element(By.CLASS_NAME, self.css_class_delete_employee_button).click()
            # Trocar por um WebDriverWait
            time.sleep(1)
            self.confirm_popup_delete_data()




        
