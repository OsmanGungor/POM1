from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from POMDemo.sites.demoqa.demobase import Basedemopage


class DemoIndexPage(Basedemopage):
    def __init__(self,driver):
        self.bookstorebutton = (By.XPATH,"//*[text()='Book Store Application']")
        super().__init__('', driver)



    def open_page(self):
        super().open_page()
        assert WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.bookstorebutton))

    def click_bookstore(self):
        assert WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.bookstorebutton))
        element= self.driver.find_element(*self.bookstorebutton)
        self.driver.execute_script("return arguments[0].scrollIntoView();",element)
        element.click()

    def get_titles(self):
        headers= self.driver.find_elements(By.XPATH,'//h5')
        headerlist = [header.accessible_name for header in headers]
        return headerlist












