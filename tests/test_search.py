
import time

from page_object.search.SearchPageObject import SearchPageObject
from page_object.menu.MenuPageObject import MenuPageObject


class Test_Search:
    def test_search_valid(self, login):
        valid_search_text = 'd'
        menu = MenuPageObject(driver=login.driver)
        search = SearchPageObject(driver=menu.driver)
        search.text_search_field(valid_search_text)
        time.sleep(3)
        assert search.text_search_valido(valid_search_text)

    def test_search_invalid(self,te amo  papai login):
        valid_search_text = 'ch'
        menu = MenuPageObject(driver=login.driver)
        search = SearchPageObject(driver=menu.driver)
        search.text_search_field(valid_search_text)
        time.sleep(3)
        assert search.text_search_invalido(valid_search_text)

