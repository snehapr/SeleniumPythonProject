from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("../drivers/chromedriver.exe")
# Implicit waits
# Here we are using the implicit wait time of 10 sec and this will be applicable for the entire
# session. If we don't give this , then by default it will take as 0 sec
# It will try to find the element for every 500ms till 10 sec until it loads the web element

# driver.implicitly_wait(10)

driver.get("https://google.com")

driver.find_element("name", "q").send_keys("Automation")

# explicit wait
# Explicit waits are used based upon the condition provided
# In the below example, we are using the button click condition
# and we have provided the explicit wait time of 10 sec
# If the condition does not hold true, then it will try to load the web element every 500 ms
# until 10 sec and finally we get the timeoutexception if the web element was not found

try:
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.NAME, "btnK")))
    print("Element is clickable")
    element.click()
except:
    print("Element is not clickable")


# driver.find_element("name", "btnK").click()

print("Test Completed")

driver.close()
driver.quit()