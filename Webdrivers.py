from selenium import webdriver

class Webdriver:
    def chrome():
        driver = webdriver.Chrome()
        return driver

    def edge():
        driver = webdriver.Edge()

    def firefox():
        driver =  webdriver.Firefox()    