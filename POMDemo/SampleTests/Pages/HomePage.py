from selenium.webdriver.common.by import By
from POMDemo.SampleTests.Locators.locators import Locators


class HomePage1:

    def __init__(self, driver):
        self.driver = driver

        # We are importing the class variables which is belonging to different class by creating
        # the objects of the class
        self.welcome_link_xpath = Locators.welcome_link_xpath
        self.logout_link_linkText = Locators.logout_link_linkText

    def welcome_click(self):
        self.driver.find_element(By.XPATH, self.welcome_link_xpath).click()

    def click_on_logout(self):
        self.driver.find_element(By.LINK_TEXT, self.logout_link_linkText).click()

