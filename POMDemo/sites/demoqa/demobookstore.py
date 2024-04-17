from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from POMDemo.sites.demoqa.demobase import Basedemopage
from selenium.webdriver.support import expected_conditions as EC


class DemoBookstorePage(Basedemopage):
    def __init__(self, driver):
        self.javabooktitle = (By.ID, "see-book-Speaking JavaScript")
        self.firstbook = (By.XPATH, "//*[@href='/books?book=9781449325862']")
        self.dropdown = (By.XPATH, "//select[@aria-label='rows per page']")
        self.searchbox = (By.ID, 'searchBox')
        self.banner = (By.XPATH, "//*[@href='https://demoqa.com']")
        self.notfound = (By.CLASS_NAME,"rt-noData")
        super().__init__('books', driver)

    def open_page(self):
        super().open_page()
        assert WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.banner))

    def get_titles(self):
        headers = self.driver.find_elements(By.CLASS_NAME, 'action-buttons')
        headerlist = [header.text for header in headers]
        return headerlist

    def clickbookname(self):
        title = self.driver.find_element(*self.firstbook)
        self.driver.execute_script("return arguments[0].scrollIntoView();", title)
        title.click()

    def chooserows(self,number):
        dropdownmenu = self.driver.find_element(*self.dropdown)
        self.driver.execute_script("return arguments[0].scrollIntoView();", dropdownmenu)
        self.driver.find_element(By.XPATH,f"//option[@value='{number}']").click()

    def getrowcount(self):
        rows=self.driver.find_elements(By.CLASS_NAME,'rt-tr-group')
        lenofrows=len(rows)
        return lenofrows

    def typeintosearch(self, word):
        searchbox = self.driver.find_element(*self.searchbox)
        searchbox.send_keys(word)

    def clickbanner(self):
        banner = self.driver.find_element(*self.banner)
        banner.click()



