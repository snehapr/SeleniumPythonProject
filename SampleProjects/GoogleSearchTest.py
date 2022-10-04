from selenium import webdriver
import unittest
import HtmlTestRunner


class GoogleSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("../drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_automation(self):
        self.driver.get("https://google.com")
        self.driver.find_element("name", "q").send_keys("Automation")
        self.driver.find_element("name", "btnK").click()
        print(self.driver.title)

    def test_search_sneha(self):
        self.driver.get("https://google.com")
        self.driver.find_element("name", "q").send_keys("Sneha")
        self.driver.find_element("name", "btnK1").click()
        print(self.driver.title)

    @classmethod
    def tearDownClass(cls):
        print("Test Completed")
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/sphaniraj/PycharmProjects/Selenium/reports'))







