# In this file we are making use of the selenium web driver example to run the unit test cases
# using the unittest module

import unittest
from selenium import webdriver

import HtmlTestRunner

class MyTestCase(unittest.TestCase):
    # If we use the setUp method , then for each test case the browser gets opened and test will get
    # executed
    # Instead of that we can make use of setUpClass method , which runs only once before all the
    # the test cases are executed
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_1(self):
        self.driver.get("https://google.com")
        self.driver.find_element("name", "q").send_keys("Automation Step by Step")
        self.driver.find_element("name", "btnK").click()
        x = self.driver.title
        print(x)
        self.assertEqual(x, "Automation Step by Step - Google Search")

    def test_search_2(self):
        self.driver.get("https://google.com")
        self.driver.find_element("name", "q").send_keys("Sneha")
        self.driver.find_element("name", "btnK").click()
        x = self.driver.title
        print(x)
        self.assertEqual(x, "Sneha - Google Search")

    # This code below is used for skipping the test
    @unittest.skip("This is a skipped test")
    def test_skip(self):
        """ This test case should be skipped """

    # Similarly instead of using the tearDown method, we can use the tearDownClass method
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

# There is option to set the verbosity levels also on the unittest module
# 0->quiet
# 1->default
# 2->verbose

# you have to run the script in the command line , then only this report gets generated and stored
# in the corresponding directory

# For the better understanding, please refer the image in the local directory


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/sphaniraj/PycharmProjects/Selenium/reports'), verbosity= 2)