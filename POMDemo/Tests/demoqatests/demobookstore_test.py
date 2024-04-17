from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from POMDemo.sites.demoqa.demobookstore import DemoBookstorePage
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

def  test_open_page(driver):
    page = DemoBookstorePage(driver)
    page.open_page()

def test_get_titles(driver):
    page = DemoBookstorePage(driver)
    page.open_page()
    page.get_titles()
    expected =['Git Pocket Guide',
               'Learning JavaScript Design Patterns',
               'Designing Evolvable Web APIs with ASP.NET',
               'Speaking JavaScript',
               "You Don't Know JS",
               'Programming JavaScript Applications',
               'Eloquent JavaScript, Second Edition',
               'Understanding ECMAScript 6']
    headerlist = page.get_titles()
    unexpected = []
    for element in headerlist:
        if element in expected:
            continue
        else:
            unexpected.append(element)
    if len(unexpected) == 0:
        assert True
    else:
        asserts.fail(f"{unexpected} = Unexpected Headers!")

def test_clickbookname(driver):
    page = DemoBookstorePage(driver)
    page.open_page()
    page.clickbookname()
    assert WebDriverWait(driver, 10).until(EC.url_to_be('https://demoqa.com/books?book=9781449325862'))

def test_typeintosearch(driver):
    page = DemoBookstorePage(driver)
    page.open_page()
    page.typeintosearch("SOME BOOK")
    assert WebDriverWait(driver, 10).until(EC.presence_of_element_located(page.notfound))


def test_clickbanner(driver):
    page = DemoBookstorePage(driver)
    page.open_page()
    page.clickbanner()
    assert WebDriverWait(driver, 10).until(EC.url_to_be('https://demoqa.com/'))


def test_chooserows(driver):
    rownumber=20
    page = DemoBookstorePage(driver)
    page.open_page()
    page.chooserows(rownumber)
    rowcount=page.getrowcount()
    assert rownumber==rowcount



