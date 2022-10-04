from selenium import webdriver

chrome_options = webdriver.ChromeOptions()

# headless option means the browser window will not appear and automation happens in the background
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="../drivers/chromedriver.exe")

driver.get("https://google.com")
print(driver.title)
driver.close()
driver.quit()
print("completed")