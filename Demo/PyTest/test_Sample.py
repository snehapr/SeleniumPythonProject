import time
import pytest
import allure
import allure_pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

# Fixtures are used to just feed some input data to the tests
# Instead of running the same code again and again in our tests, we can make use of fixtures
# and we can pass the set of fixed data so that redundancy can be reduced

# One more thing to note in pytest naming convention is that
# function name should always start with 'test' keyword
# file name should either start with 'test_<anyName>.py' or end with '<anyName>_test.py'
# If we are making use of the classes in the pytest, we should have the class name starting
# with 'Test<any_name>'

# to generate the html report, we use the below command in the command prompt
# this creates a internal CSS file also while generating the html report

# pytest --html=report2.html

# If we don't want the css file to be generated , then use the below command

# pytest --html=report2.html --self-contained-html


class TestSample:
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path="C:/Users/sphaniraj/PycharmProjects/Selenium/drivers/chromedriver_new.exe")
        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)
        # yield in pytest is similar to teardown class which we use
        # It also acts as the return keyword which we use in the python
        yield
        driver.close()
        driver.quit()
        print("Test Completed")

    # we also need to pass the test setup method to this test login function in pytest

    def test_login(self, test_setup):
        driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.find_element(By.NAME, "password").send_keys("admin123")
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()

        x = driver.title
        assert x == "OrangeHRM"

    # def test_teardown():
    #     driver.close()
    #     driver.quit()
    #     print("Test Completed")