from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
import time
import config

# setting window dimensions (one way of doing it)
# options = Options()
# options.add_argument("window-size=1366,768")

# initializing selenium driver instance
driver = webdriver.Chrome()

# setting window dimensions
print(driver.get_window_size)
driver.set_window_size(1366, 768)

# accessing website
driver.get("https://www.zoocasa.com/toronto-on-real-estate")
time.sleep(5)

# finding and clicking login button
loginButton = driver.find_element("xpath", "//a[@class='style_nav-btn__AHq2s']")
loginButton.click()

time.sleep(5)

#finding and entering username and password and signing in
usernameInput = driver.find_element("xpath", "//input[@name='email']")
usernameInput.click()
usernameInput.send_keys(config.username)

passwordInput = driver.find_element("xpath", "//input[@name='password']")
passwordInput.click()
passwordInput.send_keys(config.password)
passwordInput.send_keys("\n")

time.sleep(5)
houseDiv = driver.find_element("xpath", "//div[@class='style_wrapper__Z8WDF']")

# signInButton = driver.find_element("xpath", "//button[contains(text(), 'Sign In')]")
# signInButton.click()

for item in houseDiv:
    item.click()
    time.sleep(2)
    
