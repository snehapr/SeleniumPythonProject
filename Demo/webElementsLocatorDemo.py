from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://google.com")
time.sleep(2)

# we can directly use the first argument with the name or we can make use of the 'By' class to identify
# the web locator

searchBox = driver.find_element("name", "q")

# Some of the web locators which can be used to locate the web element (it should be unique to identify
# from the web page

# searchBox = find_element(By.ID, "id")
# searchBox = find_element(By.NAME, "q")
# searchBox = find_element(By.XPATH, "xpath")
# searchBox = find_element(By.LINK_TEXT, "link text")
# searchBox = find_element(By.PARTIAL_LINK_TEXT, "partial link text")
# searchBox = find_element(By.TAG_NAME, "tag name")
# searchBox = find_element(By.CLASS_NAME, "class name")
# searchBox = find_element(By.CSS_SELECTOR, "css selector")

searchBox.send_keys("Sneha")

time.sleep(5)

driver.close()
driver.quit()