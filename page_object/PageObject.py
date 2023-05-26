from selenium import webdriver
from selenium.webdriver.common.by import By


class PageObject:
    def __init__(self, driver=None):
        if driver:
            self.driver = driver
        else:
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(3)

    def verify_url(self, correct_url):
        return correct_url == self.driver.current_url

    def verify_title(self, correct_title, element_title):
        current_title = self.driver.find_element(By.CLASS_NAME, element_title).text
        return correct_title == current_title

