from selenium.webdriver.common.by import By
from POMDemo.SampleTests.Locators.locators import Locators


class LoginPage1:

    def __init__(self, driver):
        self.driver = driver

        # Represents the 3 locators of the login web page
        # They are username, password and login button respectively

        # We are importing the locator variables which are present in the separate file by
        # creating the object of the class
        self.username_textbox_name = Locators.username_textbox_name
        self.password_textbox_name = Locators.password_textbox_name
        self.login_button_xpath = Locators.login_button_xpath

    def enter_username(self, username):
        self.driver.find_element("name", self.username_textbox_name).clear()
        self.driver.find_element("name", self.username_textbox_name).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element("name", self.password_textbox_name).clear()
        self.driver.find_element("name", self.password_textbox_name).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()


