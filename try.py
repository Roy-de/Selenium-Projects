from selenium import webdriver
driver =  webdriver.Edge()
driver.get("https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers")
assert ("selenium") in driver.title