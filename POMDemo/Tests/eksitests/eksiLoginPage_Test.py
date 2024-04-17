
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from POMDemo.sites.eksi.eksi import Eksi
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()


def test_eksiloginpage(driver):
    site=Eksi(driver)
    site.login_page.open_page()
    site.login_page.login_fully('username','password')
    assert WebDriverWait(driver, 10).until(EC.url_to_be('https://eksisozluk.com/'))
    assert WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//nav[@id='top-navigation']//a[@href='/mesaj']")))
