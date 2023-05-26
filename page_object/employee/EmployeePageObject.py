import time

from selenium.webdriver.common.by import By

from page_object.PageObject import PageObject


class EmployeePageObject(PageObject):
    # Locators
    url_add_employee = 'https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee'
    css_type_add_button = 'oxd-button--secondary'
    add_employee_title = 'Add'
    css_name_first_name = 'firstName'
    css_name_middle_name = 'middleName'
    css_name_last_name = 'lastName'
    css_button_save = '[type="submit"]'
    css_class_toast = 'oxd-toast-container--toast'
    css_class_title_add_employee = 'orangehrm-main-title'
    css_class_name_employee = 'orangehrm-edit-employee-name'

    title_add_employee = 'Add Employee'
    first_name = 'Barbie'
    middle_name = 'Millicent'
    last_name = 'Roberts'


    def __init__(self, driver):
        super().__init__(driver=driver)

    def access_add_employee_page(self):
        buttons_list = self.driver.find_elements(By.CLASS_NAME, self.css_type_add_button)
        for i in range(len(buttons_list)):
            current_button = buttons_list[i]
            if current_button.text == self.add_employee_title:
                current_button.click()
        return self.verify_title(self.title_add_employee, self.css_class_title_add_employee) and \
            self.verify_url(self.url_add_employee)

    def add_employee(self):
        self.first_name_field()
        self.middle_name_field()
        self.last_name_field()
        self.click_button_save_employee()
        # Verificar se o toast de confirmação do cadastro é exibido
        # try:
        #     time.sleep(2)
        #     self.driver.find_element(By.CLASS_NAME, self.css_class_toast)
        #     # Melhorar a verficação do toast
        # except:
        #     return False

    def first_name_field(self):
        self.driver.find_element(By.NAME, self.css_name_first_name).send_keys(self.first_name)

    def middle_name_field(self):
        self.driver.find_element(By.NAME, self.css_name_middle_name).send_keys(self.middle_name)

    def last_name_field(self):
        self.driver.find_element(By.NAME, self.css_name_last_name).send_keys(self.last_name)

    def click_button_save_employee(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_button_save).click()

    def verify_employee_info(self):
        current_name = self.driver.find_element(By.CLASS_NAME, self.css_class_name_employee).text
        print(current_name)
        correct_name = ' '.join([self.first_name, self.last_name])
        print(correct_name)
        return correct_name == current_name


