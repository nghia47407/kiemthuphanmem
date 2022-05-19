import account
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://my.uda.edu.vn/sv/svlogin")
time.sleep(1)
driver.find_element(by=By.ID, value="User").send_keys(account.name)
time.sleep(1)
driver.find_element(by=By.ID, value="Password").send_keys(account.password)
time.sleep(1)
driver.find_element(by=By.ID, value="Lnew1").click()
time.sleep(1)
driver.find_element(by=By.CLASS_NAME, value="dropdown-toggle").click()
time.sleep(1)
driver.find_element(by=By.XPATH, value=("//ul[@class='dropdown-menu']//li[2]")).click()
driver.save_screenshot("c:\screenshot\TKB.png")
time.sleep(5)