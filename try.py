from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.get("https://finance.yahoo.com")
#assert "Python" in driver.title
elem = driver.find_element(By.NAME,"yfin-usr-qry")
elem.clear()
elem.send_keys("GBPUSD=X")
elem.send_keys(Keys.RETURN)
#assert "No result found." not in driver.page_source
time.sleep(30)
driver.close()