from selenium.webdriver.common.by import By
from POMDemo.sites.eksi.baseeksipage import Baseeksipage


class LoginPage(Baseeksipage):
    def __init__(self, driver):
        self.username_box = (By.ID, "username")
        self.password_box = (By.ID, "password")
        self.submit_button = (By.XPATH, "//button[@class='btn btn-primary btn-lg btn-block']")
        super().__init__('giris?returnUrl=https%3A%2F%2Feksisozluk.com%2F', driver)

    def login_fully(self,username,password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()


    def enter_username(self, username):
        self.driver.find_element(*self.username_box).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_box).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.submit_button).click()


