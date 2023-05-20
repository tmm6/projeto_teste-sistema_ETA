import time


class Test_Login:

    def test_login(self, open_login):
        open_login.login()
        time.sleep(3)