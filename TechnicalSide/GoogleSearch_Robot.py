import Currencies_Parsing as cp
import Stocks_Parsing as sp 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent

URL = ""
Price = ""

options = webdriver.ChromeOptions()
user_agent = UserAgent()

options.add_argument(f"user-agent={user_agent.random}")
driver = webdriver.Chrome("chromedriver.exe", 
					      options = options)

def Closing():
	global URL
	driver.close()
	driver.quit()

	sp.parse(URL)
	URL = ""

def Get_URL():
	global URL

	URL = driver.current_url
	print(URL)

	Closing()

def Search(Name):
	driver.get('https://www.google.com/')
	search_box = driver.find_element_by_name("q")

	search_box.send_keys(Name +" price")
	search_box.send_keys(Keys.RETURN)

	Get_URL()
	Price = sp.Price

	return Price
Search("3M") 