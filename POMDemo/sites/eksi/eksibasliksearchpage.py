from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

class BaslikSearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.baslik = (By.ID, "search-textbox")
        self.edit_box=(By.ID,'editbox')
        self.kenar_button=(By.ID,"save-draft-button")

    def search_baslik(self,baslik):
        self.driver.find_element(*self.baslik).send_keys(baslik,Keys.ENTER)

    def write_entry(self,entry):
        self.driver.find_element(*self.edit_box).send_keys(entry)

    def save_to_drafts(self):
        self.driver.find_element(*self.kenar_button).click()
