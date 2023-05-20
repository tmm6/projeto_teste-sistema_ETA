import time

from selenium.webdriver.common.by import By

from page_object.PageObject import PageObject


class LoginPageObject(PageObject):
    # Locators
    url = 'https://opensource-demo.orangehrmlive.com/'
    id_username = 'Admin'
    id_password = 'admin123'
    css_name_username = '[name="username"]'
    css_name_password = '[name="password"]'
    css_type_button_login = '[type="submit"]'

    def __init__(self):
        super().__init__()
        self.login_page()

    def login_page(self):
        self.driver.get(self.url)

    def login(self):
        self.username_field()
        self.password_field()
        self. loggin_button()
    def username_field(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_name_username).send_keys(self.id_username)

    def password_field(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_name_password).send_keys(self.id_password)

    def loggin_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_type_button_login).click()

    def close(self):
        self.driver.quit()


