import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://ekonobi.com/giris-yap")
driver.find_element(By.ID,"email").send_keys("osmangungor83@gmail.com")
driver.find_element(By.ID,"password").send_keys("Oksana83.")
time.sleep(3)
driver.find_element(By.XPATH, '''//button[@type="submit"]''').click()
time.sleep(3)
result=driver.find_element(By.XPATH, "//div[@class='font-medium text-xl']")
assert result.text == "OTP Doğrulama"


