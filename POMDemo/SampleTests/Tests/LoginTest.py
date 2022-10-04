from selenium import webdriver
import time
import unittest

# These 3 lines of code below has to added in the script in order to run the file from the
# import sys
# import os
# sys.path.append("C:/Users/sphaniraj/PycharmProjects/Selenium")

# Trying to import the classes present in the LoginPage.py and HomePage.py
from POMDemo.SampleTests.Pages.HomePage import HomePage1
from POMDemo.SampleTests.Pages.LoginPage import LoginPage1
import HtmlTestRunner


class LoginTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/sphaniraj/PycharmProjects/Selenium/drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        # We are using the POM (Page Object Model) implementation
        # In POM we are utilizing the classes which are present in the separate files by creating the
        # objects of the class
        # And we are also accessing the methods inside that class using the objects
        login = LoginPage1(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        home_page = HomePage1(driver)
        home_page.welcome_click()
        home_page.click_on_logout()

        # # Trying to give the username and password to the corresponding fields
        # self.driver.find_element(By.NAME, "username").send_keys("Admin")
        # self.driver.find_element(By.NAME, "password").send_keys("admin123")
        #
        # # Clicking on the Login Button
        # self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        #
        # # After the successful login, trying to click on the account drop down tab
        # self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/i").click()
        #
        # # Clicking on the logout button in that drop down list
        # self.driver.find_element(By.LINK_TEXT, "Logout").click()

        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


# This below is mainly used when we want to execute this python file from the command line
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/sphaniraj/PycharmProjects/Selenium/reports"))
