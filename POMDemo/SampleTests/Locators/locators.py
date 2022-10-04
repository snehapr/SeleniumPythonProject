# This file contains all the locator variables which are used in the web pages
# In this example it contains the locator variables belonging to both Login and Home Page

class Locators:
    # Login Page Locators
    username_textbox_name = "username"
    password_textbox_name = "password"
    login_button_xpath = "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"

    # Home Page Locators
    welcome_link_xpath = "/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/i"
    logout_link_linkText = "Logout"

