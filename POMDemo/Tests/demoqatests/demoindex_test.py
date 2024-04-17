import pytest
from selenium import webdriver
from POMDemo.sites.demoqa.demoindex import DemoIndexPage
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import asserts


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.close()
    driver.quit()


def test_demoindexpage(driver):
    page = DemoIndexPage(driver)
    page.open_page()
    page.click_bookstore()

def test_get_titles(driver):
    page = DemoIndexPage(driver)
    page.open_page()
    headerlist=page.get_titles()
    expected = ['Elements', 'Forms', 'Alerts, Frame & Windows', 'Widgets', 'Interactions','Book Store Application']
    # asserts.assert_equal(expected, headerlist,"Unexpected Header")

    unexpected=[]
    for element in headerlist:
        if element in expected:
            continue
        else:
            unexpected.append(element)
    if len(unexpected)==0:
        assert True
    else:
        asserts.fail(f"{unexpected} = Unexpected Headers!")











