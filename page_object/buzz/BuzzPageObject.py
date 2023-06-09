import time

from selenium.webdriver.common.by import By
from page_object.PageObject import PageObject

class BuzzPageObject(PageObject):
    # Locators
    ## URLs
    url_search = 'https://opensource-demo.orangehrmlive.com/web/index.php/buzz/viewBuzz'

    ## Elements
    css_enviar_post = 'oxd-buzz-post-input'
    css_curtir = 'orangehrm-heart-icon'
    css_postar = 'oxd-button--main'
    css_lista_post = 'orangehrm-buzz-post-body-text'
    css_conta_like = 'orangehrm-buzz-stats-active'
    css_opcao = 'bi-three-dots'
    css_lixo = 'bi-trash'


    #texto
    escrever_post_text = 'Fala Galera, Beleza?'
    like_esperado = '1'

    # Métodos para preencher os campos
    def text_escrever_post(self, texto):
        self.driver.find_element(By.CLASS_NAME, self.css_enviar_post).send_keys(texto)
        self.driver.find_element(By.CLASS_NAME, self.css_postar).click()
        return self.verify_toast_message('Successfully Saved')

    def text_search(self):
        time.sleep(5)
        menu_items = self.driver.find_elements(By.CLASS_NAME, self.css_lista_post)
        for item in menu_items:
            if self.escrever_post_text in item.text:
                return True
        return False
    def curtir_post(self):
        time.sleep(5)
        lista_like = self.driver.find_elements(By.CLASS_NAME, self.css_curtir)
        lista_like[0].click()
        time.sleep(5)
        menu_like = self.driver.find_elements(By.CLASS_NAME, self.css_conta_like)
        if self.like_esperado in menu_like[0].text:
            return True
        else:
            return False

    def deletar_post(self):
        time.sleep(5)
        lista_opcao = self.driver.find_elements(By.CLASS_NAME, self.css_opcao)
        lista_opcao[0].click()
        self.driver.find_element(By.CLASS_NAME, self.css_lixo).click()
        time.sleep(5)
        self.confirm_popup_delete_data()
        return self.verify_toast_message('Successfully Deleted')

