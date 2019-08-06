import unittest

from drivers.DriverInit import DriverInit
from utilites.Methods import Methods
import logging

logging.basicConfig(level=logging.INFO)

browser = "Firefox"


class TestInit(unittest.TestCase):
    def setUp(self):
        if str(browser) == "Chrome":
            self.driver = DriverInit().startChromeDriver()
        elif str(browser) == "Firefox":
            self.driver = DriverInit().startFirefoxDriver()
        self.methods = Methods(driver=self.driver)

    def tearDown(self):
        logging.info("Successfully quited the browser.")
        self.driver.quit()
