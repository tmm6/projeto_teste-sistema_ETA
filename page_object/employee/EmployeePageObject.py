import time

from selenium.webdriver.common.by import By

from page_object.PageObject import PageObject


class EmployeePageObject(PageObject):
    # Locators
    url_add_employee = 'https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee'
    css_type_add_button = 'oxd-button--secondary'
    add_employee_title = 'Add'
    css_name_first_name = 'firstName'

    def __init__(self, driver):
        super().__init__(driver=driver)

    def add_employee(self):
        #time.sleep(3)
        buttons_list = self.driver.find_elements(By.CLASS_NAME, self.css_type_add_button)
        for i in range(len(buttons_list)):
            current_button = buttons_list[i]
            if current_button.text == self.add_employee_title:
                current_button.click()
        self.first_name_field()
        time.sleep(3)
        #self.verify_url()

    def verify_url(self):
        return self.url_add_employee == self.driver.current_url

    def first_name_field(self):
        self.driver.find_element(By.NAME, self.css_name_first_name).send_keys('Thata')
