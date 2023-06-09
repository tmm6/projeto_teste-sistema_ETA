import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from page_object.PageObject import PageObject


class CandidatesVacancyPageObject(PageObject):
    # Locators
    ## URLs
    url_view_candidates = 'https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates'
    url_add_candidate = 'https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/addCandidate'

    ## Elements
    css_name_first_name = 'firstName'
    css_name_middle_name = 'middleName'
    css_name_last_name = 'lastName'
    #css_class_vacancy = 'oxd-select-text--input'
    css_class_email = 'oxd-input--active'
    css_class_contact_number = 'oxd-input--active'
    css_class_keyword = 'oxd-input--active'
    css_class_data = '??? '
    css_class_bitrash = 'bi-trash'
    css_class_notes = 'oxd-textarea--resize-vertical'
    css_button_save = '[type="submit"]'


    ## Text
    text_add_candidate_button = 'Add'
    text_title_add_candidate = 'Add Candidate'
    text_first_name = 'Caio'
    text_middle_name = 'Octavio'
    text_last_name = 'Cesar'
    text_select_vacancy = 'Senior QA Lead'
    text_email = 'caio.cesar@gmail.com'
    text_contact_number = '1998124569'
    text_palavras_chave = 'automação, líder'
    ##data
    text_notes = 'pretenção salarial de 5000'

    def __init__(self, driver):
        super().__init__(driver=driver)

    # Métodos para preencher os campos
    def first_name_field(self):
        self.driver.find_element(By.NAME, self.css_name_first_name).send_keys(self.text_first_name)

    def middle_name_field(self):
        self.driver.find_element(By.NAME, self.css_name_middle_name).send_keys(self.text_middle_name)

    def last_name_field(self):
        self.driver.find_element(By.NAME, self.css_name_last_name).send_keys(self.text_last_name)

    def vacancy_field(self):
        self.driver.find_element(By.CLASS_NAME, self.css_class_vacancy).click(self.text_select_vacancy)

    def email_field(self):
        self.driver.find_elements(By.CLASS_NAME, self.css_class_email)[3].send_keys(self.text_email)

    def contact_number_field(self):
        self.driver.find_elements(By.CLASS_NAME, self.css_class_contact_number)[4].send_keys(self.text_contact_number)

    def keywords_field(self):
        self.driver.find_elements(By.CLASS_NAME, self.css_class_keyword)[5].send_keys(self.text_palavras_chave)

    def data_field(self):
        self.driver.find_element(By.CLASS_NAME, self.css_class_data).send_keys(self)

    def notes_field(self):
        self.driver.find_element(By.CLASS_NAME, self.css_class_notes).send_keys(self.text_notes)

    def click_button_save_candidate(self):
        self.driver.find_element(By.CSS_SELECTOR, self.css_button_save).click()

    def add_candidate(self):
        time.sleep(5)
        self.driver.get(self.url_add_candidate)
        time.sleep(5)
        self.first_name_field()
        self.middle_name_field()
        self.last_name_field()
        #self.vacancy_field()
        self.email_field()
        self.contact_number_field()
        self.keywords_field()
        self.notes_field()
        time.sleep(5)
        self.click_button_save_candidate()

    def candidate_amount(self):
        self.driver.get(self.url_view_candidates)
        ## pega as lixeirinhas dos candidatos para saber quantas há, isso dará o número de cadidatos
        return len(self.driver.find_elements(By.CLASS_NAME, self.css_class_bitrash))


