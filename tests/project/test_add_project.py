import time


from page_object.menu.MenuPageObject import MenuPageObject


class Test_AddProject:
    def test_add_project(self, login):
        menu = MenuPageObject(login.driver)
        assert menu.time_option_menu(), 'Página diferente'


