from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond


class Methods():

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def click(self, scheme, locater):
        self.driver.find_element(scheme, locater).click()

    def waitForElementToPresent(self, scheme, locater):
        try:
            WebDriverWait(self.driver, 20).until(cond.visibility_of_element_located((scheme, locater)))
        except Exception:
            print(Exception)
