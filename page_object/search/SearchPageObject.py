import time

from selenium.webdriver.common.by import By
from page_object.PageObject import PageObject


class SearchPageObject(PageObject):
    # Locators
    ## URLs
    url_search = 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'

    ## Elements
    css_name_search = 'oxd-input--active'
    class_list_options_menu = 'oxd-main-menu-item--name'


    def __init__(self, driver):
        super().__init__(driver=driver)

    # Métodos para preencher os campos
    def text_search_field(self, texto):
        self.driver.find_element(By.CLASS_NAME, self.css_name_search).send_keys(texto)

    def text_search_valido(self, texto):
        menu_items = self.driver.find_elements(By.CLASS_NAME, texto)
        for item in menu_items:
            print(item.text)
            if texto not in item.text:
                return False
        return True

    def text_search_invalido(self, texto):
        menu_items = self.driver.find_elements(By.CLASS_NAME, texto)
        if menu_items.__len__() != 0:
            return False
        else:
            return True

