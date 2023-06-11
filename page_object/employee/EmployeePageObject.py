import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from page_object.PageObject import PageObject


class EmployeePageObject(PageObject):
    # Locators
    ## URLs
    url_add_employee = 'https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee'

    ## Elements
    css_name_first_name = 'firstName'
    css_name_middle_name = 'middleName'
    css_name_last_name = 'lastName'
    css_button_save = '[type="submit"]'
    css_class_title_add_employee = 'orangehrm-main-title'
    css_class_name_employee = 'orangehrm-edit-employee-name'
    css_placeholder_employee_name = '[placeholder="Type for hints..."]'
    css_class_cells_employees = '[role = "cell"]'
    css_class_delete_employee_button = 'bi-trash'
    css_class_titles_profile_info = 'orangehrm-main-title'
    css_class_amount_of_search_result = 'orangehrm-vertical-padding'


    ## Text
    text_add_employee_button = 'Add'
    text_search_employee = 'Search'
    text_title_add_employee = 'Add Employee'
    text_first_name = 'Barbie'
    text_middle_name = 'Millicent'
    text_last_name = 'Roberts'
    text_toast_msg_create = 'Successfully Saved'
    text_toast_msg_delete = 'Successfully Deleted'
    text_toast_msg_not_found_search = 'No Records Found'
    text_toast_msg_found_search = '(1) Record Found'
    text_list_titles_profile_employee = ['Personal Details', 'Custom Fields', 'Attachments']

    def __init__(self, driver):
        super().__init__(driver=driver)

    def first_name_field(self):
        self.driver.find_element(By.NAME, self.css_name_first_name).send_keys(self.text_first_name)

    def middle_name_field(self):
        self.driver.find_element(By.NAME, self.css_name_middle_name).send_keys(self.text_middle_name)

    def last_name_field(self):
        self.driver.find_element(By.NAME, self.css_name_last_name).send_keys(self.text_last_name)

    def click_button_save_employee(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_button_save).click()

    def access_add_employee_page(self):
        self.click_correct_button(expect_title=self.text_add_employee_button)
        return self.verify_title(self.text_title_add_employee, self.css_class_title_add_employee) and \
            self.verify_url(self.url_add_employee)

    def verify_employee_name(self):
        time.sleep(5)
        current_name = WebDriverWait(self.driver, timeout=12).until(
            lambda name_element: name_element.find_element(By.CLASS_NAME, self.css_class_name_employee))
        name = ''.join([self.text_first_name, self.text_last_name])
        return name == current_name.text.replace(' ', '')

    def verify_employee_profile_titles(self):
        # Alterar para outro tipo de espera.
        time.sleep(4)
        titles_list = WebDriverWait(self.driver, timeout=10).until(
            lambda titles_element: titles_element.find_elements(By.CLASS_NAME, self.css_class_titles_profile_info))
        for i in range(len(titles_list)):
            if titles_list[i].text != self.text_list_titles_profile_employee[i]:
                return False
        return True

    def verify_search_result(self):
        time.sleep(3)
        result = self.driver.find_element(By.CLASS_NAME, self.css_class_amount_of_search_result)
        if result.text == self.text_toast_msg_not_found_search:
            return self.verify_toast_message(self.text_toast_msg_not_found_search)
        else:
            list_employees = self.driver.find_elements(By.CSS_SELECTOR, self.css_class_cells_employees)
            name = ' '.join([self.text_first_name, self.text_middle_name])
            assert_name = list_employees[2].text == name
            assert_amount_result = result.text == self.text_toast_msg_found_search
            return assert_name and assert_amount_result

    def add_employee(self):
        # Método para adicionar um usuário. Ao final é verificado o toast.
        time.sleep(3)
        self.first_name_field()
        self.middle_name_field()
        self.last_name_field()
        self.click_button_save_employee()
        return self.verify_toast_message(self.text_toast_msg_create)

    def search_employee(self):
        time.sleep(3)
        list_elements_search = self.driver.find_elements(By.CSS_SELECTOR, self.css_placeholder_employee_name)
        employee_name = list_elements_search[0]
        # Este if verifica se já existe algo digitado no campo. Caso tenha ele irá apagar o conteúdo.
        if employee_name.get_attribute('value'):
            employee_name.send_keys(Keys.SHIFT + Keys.HOME + Keys.DELETE)

        employee_name.send_keys(self.text_first_name)
        self.click_correct_button(expect_title=self.text_search_employee)

    def delete_employee(self):
        time.sleep(3)
        self.driver.find_element(By.CLASS_NAME, self.css_class_delete_employee_button).click()
        time.sleep(3)
        self.confirm_popup_delete_data()
        time.sleep(3)
        return self.verify_toast_message(self.text_toast_msg_delete)







        
