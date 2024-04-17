from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from POMDemo.sites.eksi.baseeksipage import Baseeksipage


class EksiIndex(Baseeksipage):
    def __init__(self, driver):
        self.driver = driver
        self.giris_ilk = (By.ID, "top-login-link")
        self.logo = (By.ID, 'logo')
        super().__init__('', driver)

    def open_page(self):
        self.driver.get(self.url)
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.logo))

    def click_enter(self):
        self.driver.find_element(*self.giris_ilk).click()
        WebDriverWait(self.driver, 5).until(EC.url_to_be(self.baseurl+'giris?returnUrl=https%3A%2F%2Feksisozluk.com%2F'))

