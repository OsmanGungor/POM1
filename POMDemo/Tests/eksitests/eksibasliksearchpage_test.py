import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

from POMDemo.sites.eksi.eksi import Eksi


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()

def test_eksibasliksearchpage(driver):
    site=Eksi(driver)
    site.login_page.open_page()
    site.login_page.login_fully('username','password')
    site.write_entry.search_baslik("kayseri")
    assert WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[@itemprop='name']")))
    site.write_entry.write_entry("memleket")
    site.write_entry.save_to_drafts()
    assert WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "draft-content")))

