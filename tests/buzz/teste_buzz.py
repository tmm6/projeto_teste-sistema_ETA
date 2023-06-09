
import time

from page_object.buzz.BuzzPageObject import BuzzPageObject
from page_object.menu.MenuPageObject import MenuPageObject


class Teste_Buzz:
    def test_escrever_post(self, login):
        enviar_post_text = 'Fala Galera, Beleza?'
        menu = MenuPageObject(driver=login.driver)
        assert menu.buzz_option_menu(), 'Página diferente'
        buzz = BuzzPageObject(driver=menu.driver)
        time.sleep(5)
        assert buzz.text_escrever_post(enviar_post_text), 'Post não Publicado'
        assert buzz.text_search(), 'Apareceu!!!'

    def test_validar_curtida(self,login):
        menu = MenuPageObject(driver=login.driver)
        assert menu.buzz_option_menu(), 'Página diferente'
        buzz = BuzzPageObject(driver=menu.driver)
        time.sleep(5)
        assert buzz.curtir_post(), 'Like não encontrado'

    def test_verificar_deletar_post(self,login):
        menu = MenuPageObject(driver=login.driver)
        assert menu.buzz_option_menu(), 'Página diferente'
        buzz = BuzzPageObject(driver=menu.driver)
        time.sleep(5)
        assert buzz.deletar_post(), 'Não Deletou'





