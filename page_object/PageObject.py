from selenium import webdriver
from selenium.webdriver.common.by import By


class PageObject:
    #Locators
    ## Elements
    css_type_add_button = 'oxd-button--secondary'
    css_class_option_popup_delete = 'orangehrm-button-margin'

    ## Texts
    text_confirm_popup_delete = 'Yes'

    def __init__(self, driver=None):
        if driver:
            self.driver = driver
        else:
            self.driver = webdriver.Chrome()
            # Ajustar tamanho da tela
            self.driver.set_window_size(1200, 920)
            self.driver.implicitly_wait(3)

    def verify_url(self, correct_url):
        return correct_url == self.driver.current_url

    def verify_title(self, correct_title, element_title):
        current_title = self.driver.find_element(By.CLASS_NAME, element_title).text
        return correct_title == current_title

    def click_correct_button(self, element=css_type_add_button, expect_title=""):
        """
        Este método irá clicar no botão de Search ou de +Add. A escolha é de acordo com o parâmetro "expect_title"
        O método consiste em realizar uma busca por todos os elementos que correspondem ao botão.
        Em seguida, compara cada elemento da lista de elementos encontrados com o botão Search ou Add em que a
        escolha é passada por parâmetro.
        Por fim, clica no botão.
        """
        buttons_list = self.driver.find_elements(By.CLASS_NAME, element)
        for i in range(len(buttons_list)):
            current_button = buttons_list[i]
            if current_button.text == expect_title:
                current_button.click()

    def confirm_popup_delete_data(self, option=text_confirm_popup_delete):
        """
        Este método pode ser utilizado quando se tem popups de confirmação de exclusão de algum dado.
        :param option: Representa a escolha de qual opção no popup é selecionada. Pode ser Cancelar ou Confirmar.
        :return: O dado é deletado ou não de acordo com o parâmetro
        """
        options_popup_delete = self.driver.find_elements(By.CLASS_NAME, self.css_class_option_popup_delete)
        for i in range(len(options_popup_delete)):
            current_option = options_popup_delete[i]
            if option in current_option.text:
                current_option.click()
