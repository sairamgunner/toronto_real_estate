from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import config
import pandas as pd
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# loading environment variables from .env file
load_dotenv()

# creating MongoDB connection object
client = MongoClient(os.environ.get("MONGODB_URI"))

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
driver.get("https://www.zoocasa.com/toronto-on-real-estate/sold?")

time.sleep(5)
houseDiv = driver.find_elements("xpath", "//div[@class='style_wrapper__Z8WDF']")
   
def scrapeAndCollectInDataFrame():
    pageNumber = 0 # Change the start page number
    # maxPageNumber = 250 # Change the max page number
    maxPageNumber = driver.find_element("xpath", "//*[@id='__next']/div[1]/div[3]/div/div[2]/div[4]/div/nav/ul/li[8]/button").text
    # initializing empty lists for pandas to .csv file implementation
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
    levels = []
    garage = []
    taxes = []
    walk_score = []
    ride_score = []
    bike_score = []
    maintenance_fees = []

    for page in range (1, int(maxPageNumber) + 1, 1):
    # for page in range (1, 2, 1):
        pageNumber += 1
        driver.get("https://www.zoocasa.com/toronto-on-real-estate/sold?" + "page=" + str(pageNumber))
        time.sleep(3)
        for item in driver.find_elements("xpath", "//div[@class='style_wrapper__Z8WDF']"):
            item.click()
            time.sleep(2)
            linkURL = driver.find_element("xpath", "//*[@id='listing']/div[1]/div/a")
            title.append(driver.find_element("xpath", "//*[@id='listing']/div[3]/span[1]/div[1]/div[1]/div[1]/span[2]/span[1]/a/h1").text)
            final_price.append(driver.find_element("xpath", "//*[@id='listing']/div[3]/span[1]/div[1]/div[1]/div[2]/span/div/div/div[1]").text)
            list_price.append(driver.find_element("xpath", "//*[@id='listing']/div[3]/span[1]/div[1]/div[1]/div[2]/span/div/div/div[2]/span").text)
            bedrooms.append(driver.find_element("xpath", "//*[@id='listing']/div[3]/span[1]/div[1]/div[1]/div[1]/div/div/span[1]").text)
            bathrooms.append(driver.find_element("xpath", "//*[@id='listing']/div[3]/span[1]/div[1]/div[1]/div[1]/div/div/span[2]").text)
            sqft.append(driver.find_element("xpath", "//*[@id='listing']/div[3]/span[1]/div[1]/div[1]/div[1]/div/div/span[3]").text)
            parking.append(driver.find_element("xpath", "//*[@id='listing']/div[3]/span[1]/div[1]/div[1]/div[1]/div/div/span[4]").text)
            type.append(driver.find_element("xpath", "//*[@id='listing']/div[3]/span[1]/div[1]/div[1]/div[1]/span[2]/span[1]/a/h1/span").text)
            levels.append(driver.find_element("xpath", "//*[@id='listing']/div[3]/span[1]/div[2]/div/div/div/section/section/div[2]/span[2]").text)
            garage.append(driver.find_element("xpath", "//*[@id='listing']/div[3]/span[1]/div[2]/div/div/div/section/section/div[4]/span[2]").text)
            full_link.append(linkURL.get_attribute("href"))
            full_address.append(driver.find_element("xpath", "//*[@id='listing']/div[3]/span[1]/div[2]/div/div/div/section/p[1]").text)
            maintenance_fees.append(driver.find_element("xpath", "//*[@id='listing']/div[3]/span[1]/div[2]/div/div/div/section/section/div[5]/span[2]").text)
            taxes.append(driver.find_element("xpath", "//*[@id='listing']/div[3]/span[1]/div[2]/div/div/div/section/section/div[6]/span[2]").text)            

            driver.find_element("xpath", "//*[@id='listing']/div[3]/span[1]/div[2]/ul/li[2]").click()

            description.append(driver.find_element("xpath", "//*[@id='listing']/div[3]/span[1]/div[2]/div/div/div[1]/section/p/section").text)
            mls.append(driver.find_element("xpath", "//*[@id='listing']/div[3]/span[1]/div[2]/div/div/div[3]/section/section/div[1]/span[2]").text)
            time.sleep(2)
            walk_score.append(driver.find_element("xpath", "//*[@id='listing']/div[3]/span[1]/div[2]/div/div/div[2]/section[1]/div[1]/a/div").text)
            ride_score.append(driver.find_element("xpath", "//*[@id='listing']/div[3]/span[1]/div[2]/div/div/div[2]/section[2]/div[1]/a/div").text)
            bike_score.append(driver.find_element("xpath", "//*[@id='listing']/div[3]/span[1]/div[2]/div/div/div[2]/section[3]/div[1]/a/div").text)

            linkURL.send_keys(Keys.ESCAPE)
            # time.sleep(5)
    
    data = pd.DataFrame(
    {
        'title': title,
        'final_price': final_price,
        'list_price': list_price,
        'bedrooms': bedrooms,
        'bathrooms': bathrooms,
        'sqft': sqft,
        'parking': parking,
        'description': description,
        'mls': mls,
        'type': type,
        'full_link': full_link,
        'full_address': full_address,
        'levels': levels,
        'garage': garage,
        'maintenance_fees': maintenance_fees,
        'taxes': taxes,
        'walk_score': walk_score,
        'ride_score': ride_score,
        'bike_score': bike_score
    })
    data.to_excel('data.xlsx')
    

def scrapeAndInsertInMongoDB():
    pageNumber = 0 # Change the start page number
    # maxPageNumber = 250 # Change the max page number
    maxPageNumber = driver.find_element("xpath", "//*[@id='__next']/div[1]/div[3]/div/div[2]/div[4]/div/nav/ul/li[8]/button").text
    for page in range (1, int(maxPageNumber) + 1, 1):
        pageNumber += 1
        driver.get("https://www.zoocasa.com/toronto-on-real-estate/sold?" + "page=" + str(pageNumber))
        time.sleep(3)
        for item in driver.find_elements("xpath", "//div[@class='style_wrapper__Z8WDF']"):
            item.click()
            time.sleep(2)
            linkURL = driver.find_element("xpath", "//*[@id='listing']/div[1]/div/a")

            # assigning variables for mongodb
            _title = driver.find_element("xpath", "//*[@id='listing']/div[3]/span[1]/div[1]/div[1]/div[1]/span[2]/span[1]/a/h1").text
            _final_price = driver.find_element("xpath", "//*[@id='listing']/div[3]/span[1]/div[1]/div[1]/div[2]/span/div/div/div[1]").text
            _list_price = driver.find_element("xpath", "//*[@id='listing']/div[3]/span[1]/div[1]/div[1]/div[2]/span/div/div/div[2]/span").text
            _bedrooms = driver.find_element("xpath", "//*[@id='listing']/div[3]/span[1]/div[1]/div[1]/div[1]/div/div/span[1]").text
            _bathrooms = driver.find_element("xpath", "//*[@id='listing']/div[3]/span[1]/div[1]/div[1]/div[1]/div/div/span[2]").text
            _sqft = driver.find_element("xpath", "//*[@id='listing']/div[3]/span[1]/div[1]/div[1]/div[1]/div/div/span[3]").text
            _parking = driver.find_element("xpath", "//*[@id='listing']/div[3]/span[1]/div[1]/div[1]/div[1]/div/div/span[4]").text
            _type = driver.find_element("xpath", "//*[@id='listing']/div[3]/span[1]/div[1]/div[1]/div[1]/span[2]/span[1]/a/h1/span").text
            _levels = driver.find_element("xpath", "//*[@id='listing']/div[3]/span[1]/div[2]/div/div/div/section/section/div[2]/span[2]").text
            _garage = driver.find_element("xpath", "//*[@id='listing']/div[3]/span[1]/div[2]/div/div/div/section/section/div[4]/span[2]").text
            _taxes = driver.find_element("xpath", "//*[@id='listing']/div[3]/span[1]/div[2]/div/div/div/section/section/div[6]/span[2]").text
            _maintenance_fees = driver.find_element("xpath", "//*[@id='listing']/div[3]/span[1]/div[2]/div/div/div/section/section/div[5]/span[2]").text        
            _full_link = linkURL.get_attribute("href")
            _full_address = driver.find_element("xpath", "//*[@id='listing']/div[3]/span[1]/div[2]/div/div/div/section/p[1]").text

            driver.find_element("xpath", "//*[@id='listing']/div[3]/span[1]/div[2]/ul/li[2]").click()

            #assigning variables for mongodb
            time.sleep(2)
            _description = driver.find_element("xpath", "//*[@id='listing']/div[3]/span[1]/div[2]/div/div/div[1]/section/p/section").text
            _mls = driver.find_element("xpath", "//*[@id='listing']/div[3]/span[1]/div[2]/div/div/div[3]/section/section/div[1]/span[2]").text
            _taxes = driver.find_element("xpath", "//*[@id='listing']/div[3]/span[1]/div[2]/div/div/div[2]/section[1]/div[1]/a").text
            _walk_score = driver.find_element("xpath", "//*[@id='listing']/div[3]/span[1]/div[2]/div/div/div[2]/section[1]/div[1]/a").text
            _ride_score = driver.find_element("xpath", "//*[@id='listing']/div[3]/span[1]/div[2]/div/div/div[2]/section[2]/div[1]/a").text
            _bike_score = driver.find_element("xpath", "//*[@id='listing']/div[3]/span[1]/div[2]/div/div/div[2]/section[3]/div[1]/a").text

            # time.sleep(2)
            linkURL.send_keys(Keys.ESCAPE)
            client.capstone.webscrapingv2.insert_one(
                {
                    'title': _title,
                    'final_price': _final_price,
                    'list_price': _list_price,
                    'bedrooms': _bedrooms,
                    'bathrooms': _bathrooms,
                    'sqft': _sqft,
                    'parking': _parking,
                    'description': _description,
                    'mls': _mls,
                    'levels': _levels,
                    'garage': _garage,
                    'type': _type,
                    'taxes': _taxes,
                    'maintenance_fees': _maintenance_fees,
                    'full_link': _full_link,
                    'full_address': _full_address,
                    'walk_score': _walk_score,
                    'ride_score': _ride_score,
                    'bike_score': _bike_score
                }
            )
            # time.sleep(5)

scrapeAndCollectInDataFrame()
#scrapeAndInsertInMongoDB()