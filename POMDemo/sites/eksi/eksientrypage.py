from selenium.webdriver.common.by import By

class EntryWritePage:
    def __init__(self, driver):
        self.driver = driver
        self.edit_box = (By.ID, 'editbox')
        self.kenar_button = (By.ID, "save-draft-button")
    def write_entry(self,entry):
        self.driver.find_element(*self.edit_box).send_keys(entry)

    def save_to_drafts(self):
        self.driver.find_element(*self.kenar_button).click()