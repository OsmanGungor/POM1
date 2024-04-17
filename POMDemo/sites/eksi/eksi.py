from POMDemo.sites.eksi.eksiIndexpage import EksiIndex
from POMDemo.sites.eksi.eksiLoginPage import LoginPage
from POMDemo.sites.eksi.eksibasliksearchpage import BaslikSearchPage


class Eksi():
    def __init__(self,driver):
        self.index_page=EksiIndex(driver)
        self.login_page=LoginPage(driver)
        self.write_entry=BaslikSearchPage(driver)
