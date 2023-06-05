import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from page_object.PageObject import PageObject


class CandidatePageObject(PageObject):
    # Locators
    ## URLs
    url = 'https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates'
    ## Elements
    css_vacancy_name = 'oxd-input--active'
    css_job_title = 'oxd-select-text--active'
    css_description_textarea = 'oxd-textarea--resize-vertical'
    css_delete_icon = 'bi-trash'

    def __init__(self, driver):
        super().__init__(driver=driver)

    # Métodos para preencher os campos
    def delete_candidate(self):
        self.driver.get(self.url)

        elements = self.driver.find_elements(By.CLASS_NAME, 'bi-trash')
        candidateAmountBefore = len(elements)
        print('Quantidade: ', candidateAmountBefore)

        if candidateAmountBefore == 0:
            return False

        first = elements.__getitem__(0)
        first.click()
        time.sleep(5)
        popup = self.driver.find_element(By.CLASS_NAME, 'orangehrm-dialog-popup')
        button = popup.find_element(By.CLASS_NAME, 'oxd-button-icon')
        button.click()
        time.sleep(5)
        candidatesAfter = self.driver.find_elements(By.CLASS_NAME, 'bi-trash')
        candidateAmountAfter = len(candidatesAfter)
        print('Quantidade depois: ', candidateAmountAfter)
        if(candidateAmountAfter < candidateAmountBefore):
            return True
        else:
            return False


        #'oxd-buton-icon'


