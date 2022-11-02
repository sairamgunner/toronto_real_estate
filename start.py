from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import config
import pandas as pd

# setting window dimensions (one way of doing it)
# options = Options()
# options.add_argument("window-size=1366,768")

# initializing selenium driver instance
driver = webdriver.Chrome(ChromeDriverManager().install())

# setting window dimensions
print(driver.get_window_size)
# driver.set_window_size(1366, 768)
driver.maximize_window()

# accessing website
# driver.get("https://www.zoocasa.com/toronto-on-real-estate")
driver.get("https://www.zoocasa.com/toronto-on-sold-listings?")
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

time.sleep(2)
driver.get("https://www.zoocasa.com/toronto-on-sold-listings")

time.sleep(5)
houseDiv = driver.find_elements("xpath", "//div[@class='style_wrapper__Z8WDF']")

# signInButton = driver.find_element("xpath", "//button[contains(text(), 'Sign In')]")
# signInButton.click()

pageNumber = 0
maxPageNumber = driver.find_element("xpath", "//*[@id='__next']/div[1]/div[3]/div/div[2]/div[4]/div/nav/ul/li[8]/button").text
title = []
final_price = []
list_price = []
bedrooms = []
bathrooms = []
sqft = []
parking = []
description = []
mls = []
type = []
full_link = []
full_address = []

for page in range (1, int(maxPageNumber) + 1, 1):
    pageNumber += 1
    driver.get("https://www.zoocasa.com/toronto-on-sold-listings?" + "page=" + str(pageNumber))
    time.sleep(3)
    for item in driver.find_elements("xpath", "//div[@class='style_wrapper__Z8WDF']"):
        item.click()
        time.sleep(2)
        linkURL = driver.find_element("xpath", "//*[@id='listing']/div[1]/div/a")
        title.append(driver.find_element("xpath", "//*[@id='listing']/div[3]/span[1]/div[1]/div[1]/div[1]/span[2]/span[1]/a/h1").text)
        final_price.append(driver.find_element("xpath", "//*[@id='listing']/div[3]/span[1]/div[1]/div[1]/div[2]/span/div/div/div[1]").text)
        list_price.append(driver.find_element("xpath", "//*[@id='listing']/div[3]/span[1]/div[1]/div[1]/div[2]/span/div/div/div[2]/span").text)
        bedrooms.append(driver.find_element("xpath", "//*[@id='listing']/div[3]/span[1]/div[1]/div[1]/div[1]/div/div/span[1]").text)
        sqft.append(driver.find_element("xpath", "//*[@id='listing']/div[3]/span[1]/div[1]/div[1]/div[1]/div/div/span[3]").text)
        parking.append(driver.find_element("xpath", "//*[@id='listing']/div[3]/span[1]/div[1]/div[1]/div[1]/div/div/span[4]").text)
        type.append(driver.find_element("xpath", "//*[@id='listing']/div[3]/span[1]/div[1]/div[1]/div[1]/span[2]/span[1]/a/h1/span").text)
        full_link.append(linkURL.get_attribute("href"))
        full_address.append(driver.find_element("xpath", "//*[@id='listing']/div[3]/span[1]/div[2]/div/div/div/section/p[1]").text)
        driver.find_element("xpath", "//*[@id='listing']/div[3]/span[1]/div[2]/ul/li[2]").click()
        description.append(driver.find_element("xpath", "//*[@id='listing']/div[3]/span[1]/div[2]/div/div/div[1]/section/p/section").text)
        mls.append(driver.find_element("xpath", "//*[@id='listing']/div[3]/span[1]/div[2]/div/div/div[3]/section/section/div[1]/span[2]").text)
        time.sleep(2)
        linkURL.send_keys(Keys.ESCAPE)
        time.sleep(5)

data = pd.DataFrame(
    {
        'title': title,
        'final_price': final_price,
        'list_price': list_price,
        'bedrooms': bedrooms,
        'sqft': sqft,
        'parking': parking,
        'description': description,
        'mls': mls,
        'type': type,
        'full_link': full_link,
        'full_address': full_address
    }
)
    
data.to_excel('data.xlsx')