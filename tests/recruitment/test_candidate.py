
import time

from page_object.search.SearchPageObject import SearchPageObject
from page_object.recruitment.CandidatePageObject import CandidatePageObject
from page_object.menu.MenuPageObject import MenuPageObject


class Test_Delete_Canditade:
    def test_delete_candidate(self, login):
        menu = MenuPageObject(driver=login.driver)
        candidate = CandidatePageObject(driver=menu.driver)
        time.sleep(3)
        assert candidate.delete_candidate()
        time.sleep(3)




