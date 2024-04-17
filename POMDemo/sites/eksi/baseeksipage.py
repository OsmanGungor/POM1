class Baseeksipage():
    def __init__(self, url, driver):
        self.driver = driver
        self.baseurl='https://eksisozluk.com/'
        self.url = self.baseurl+ url

    def open_page(self):
        self.driver.get(self.url)
