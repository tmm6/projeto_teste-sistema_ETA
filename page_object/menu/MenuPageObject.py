import time

from selenium.webdriver.common.by import By
from page_object.PageObject import PageObject


class MenuPageObject(PageObject):
    # Locators

    class_list_options_menu = 'oxd-main-menu-item--name'

    menu_time = 'Time'
    menu_recruitment = 'Recruitment'
    menu_admin = 'Admin'
    menu_directory = 'Directory'
    menu_pim = 'PIM'

    url_time_page = 'https://opensource-demo.orangehrmlive.com/web/index.php/time/viewEmployeeTimesheet'
    url_recruitment = 'https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates'
    url_admin = 'https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers'
    url_directory = 'https://opensource-demo.orangehrmlive.com/web/index.php/directory/viewDirectory'
    url_employee = 'https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList'

    def __init__(self, driver):
        super().__init__(driver=driver)

    def open_menu_item(self, item_name, url_page):
        menu_items = self.driver.find_elements(By.CLASS_NAME, self.class_list_options_menu)
        for item in menu_items:
            if item.text == item_name:
                item.click()
                return url_page == self.driver.current_url
        return False

    def time_option_menu(self):
        return self.open_menu_item(self.menu_time, self.url_time_page)

    def recruitment_option_menu(self):
        return self.open_menu_item(self.menu_recruitment, self.url_recruitment)

    def admin_option_menu(self):
        return self.open_menu_item(self.menu_admin, self.url_admin)

    def directory_option_menu(self):
        return self.open_menu_item(self.menu_directory, self.url_directory)

    def pim_option_menu(self):
        return self.open_menu_item(self.menu_pim, self.url_employee)
