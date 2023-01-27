# Importing libraries
from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# Variables
url = "https://www.tripadvisor.in/Restaurants-g304554-Mumbai_Maharashtra.html"
data = []
options = {}  # No need of options because I am not using any proxy

# Setting up driver and beautiful soup find_all
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)

soup = BeautifulSoup(driver.page_source, "lxml")

restaurants = soup.find_all("div", class_="zdCeB Vt o")


# Running a loop to find and log data
for restaurant in restaurants:

    restaurant_name = restaurant.find('a').text
    restaurant_url = "https://www.tripadvisor.in" + \
        restaurant.find("a")['href']

    # print(restaurant_name)
    # print(restaurant_url)
    driver.get(restaurant_url)

    soup2 = BeautifulSoup(driver.page_source, "lxml")

    # Restaurant stars rating out of 5 in float value
    rating = float(soup2.find("svg", class_="UctUV d H0")
                   ["aria-label"].split(" ")[0].strip())

    # Restaurant rank in the target city
    rank = soup2.find("div", class_="cNFlb").text.split(" ")[0]

    # Price and Cuisine of the restaurant
    # Prices and Cuisines are concatenated, I have left it to be
    price_cuisine = soup2.find("span", class_="DsyBj DxyfE").text

    # Address of the restaurant
    address = soup2.find_all("span", class_="DsyBj cNFrA")[1].text

    # Contact number
    contact = soup2.find_all("span", class_="DsyBj cNFrA")[2].text

    # Appending to everything
    data.append({
        "Name": restaurant_name,
        "Rank": rank,
        "Rating": rating,
        "Price&cuisine": price_cuisine,
        "Contact": contact,
        "Address": address
    })

# Creating dataframe, importing data and exporting to CSV with no index
df = pd.DataFrame(data)
df.to_csv("./restaurant_scraped_list.csv", index=False)
