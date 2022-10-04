
# web driver module can be directly used in the projects without having to install the web brower drivers
# like how we installed in the previous examples (chromedriver.exe)

# In this example we can see that we are using the webdriver manager class to import the Chrome driver
# without having to explicity install the chrome driver

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://google.com")
time.sleep(2)

driver.close()
driver.quit()

