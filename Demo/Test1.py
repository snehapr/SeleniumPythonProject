import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


options = webdriver.ChromeOptions()
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")


driver = webdriver.Chrome(chrome_options=options, executable_path="../drivers/chromedriver.exe")
driver.set_page_load_timeout(10)

driver.get("https://google.com")
driver.find_element("name", "q").send_keys("dogs breeds")
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable(("name", "btnK"))).click()

# driver.find_element("name","btnK").click()
# sometimes this click function might not work as the search results will overlap the search button
# so alternative to that we can use the send_keys(Keys.ENTER) or send_keys(Keys.ENTER)
# its just as clicking the enter button on the keyboard

# also the sleep time also should be introduced to escape from the excetion raised
time.sleep(10)


driver.find_element("name", "btnK").send_keys(Keys.RETURN)


driver.close()
driver.quit()

print("test completed")