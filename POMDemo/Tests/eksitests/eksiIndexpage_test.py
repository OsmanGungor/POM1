import pytest
from selenium import webdriver

from POMDemo.sites.eksi.eksi import Eksi
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()

def test_eksiIndexpage(driver):
    site=Eksi(driver)
    site.index_page.open_page()
    site.index_page.click_enter()

