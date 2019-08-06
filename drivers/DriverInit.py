from selenium import webdriver
import logging

logging.basicConfig(level=logging.INFO)

class DriverInit():
    def startChromeDriver(self):
        driver = webdriver.Chrome(executable_path="C:\AutomationDrivers\chromedriver.exe")
        driver.maximize_window()
        driver.get("https://www.google.com")
        logging.info("Generated Chrome Driver")
        return driver

    def startFirefoxDriver(self):
        driver = webdriver.Firefox(executable_path="C:\AutomationDrivers\geckodriver.exe")
        driver.maximize_window()
        driver.get("https://www.google.com")
        logging.info("Generated FireFox Driver")
        return driver
