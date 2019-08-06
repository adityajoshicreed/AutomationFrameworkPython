from selenium.webdriver.common.by import By

from base.TestInit import TestInit
import unittest


class SampleTest(TestInit,unittest.TestCase):
    def test_search_google(self):
        self.driver.find_element_by_name("q").send_keys("Hello")
        self.methods.waitForElementToPresent(By.CLASS_NAME,"gNO89b")
        self.methods.click(By.CLASS_NAME,"gNO89b")
        assert "Google" in self.driver.title


# if __name__ == '__main__':
#     unittest.main()