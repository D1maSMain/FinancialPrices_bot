import requests # For Http requests
import sqlite3 # For working with SQLite database
from bs4 import BeautifulSoup # For working with Html Script
import re # For regexs
import os
import fileinput
import time
from fake_useragent import UserAgent
from datetime import datetime

user_agent = UserAgent()
HEADERS = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36",
           'accept': '*/*'} # Using headers
print(HEADERS)

User = "" # Current User

Time = datetime.now().hour*60 + datetime.now().minute

def get_Html(url, params = None): # Func. that returns script
    #global user_agent
    #HEADERS['user-agent'] = user_agent.chrome
    time.sleep(1)
    result = requests.get(url, headers=HEADERS, params=params) # Making Http request
    return result

def write_Data(Name, Price,StartFollow, userid, FC):
    global Time

    DateTimeFormat = "%Y/%m/%d-%H:%M"
    Now = datetime.now().strftime(DateTimeFormat) # Making value with date
    print(Now)
    if FC == True:
        path = os.path.abspath(os.curdir) + "\\Name-Prices_Files"
    else:
        path = os.path.abspath(os.curdir) + "\\TechnicalSide\\Name-Prices_Files"
    
    F = open(path + "\\Stock\\{}".format(userid) +".txt", "a+") # Making file | Check it made

    F.close()

    F = open(path + "\\Stock\\{}".format(userid) +".txt", "r") # Open for reading
    Text = "" # Whole text in file

    for line in F: # Walking on the lines in file
        if re.match(".+:.+", line) != None:

            Data = re.match(".+:.+", line).group(0)

            if StartFollow == None:
                #print("https://www.google.com/search?q=" + re.search("[\w\s]+", Data).group(0) + "+price")
                Price = parse("https://www.google.com/search?q=" + re.search("[\w\s]+", Data).group(0) + "+price", None, None)

            elif re.search("\w+\:", Data).group(0) == Name + ":" and StartFollow == True:
                print("Exist")
                return

            elif re.search("[\w\s]+\:", Data).group(0) == Name + ":" and StartFollow == False:
                Text += ""
                print(False)
                continue

            High_Wick = re.search(r"\(\d+\.\d", Data).group(0)
            Low_Wick = re.search(r"\d+\.\d\)", Data).group(0)

            if Data[-1] == ";":
                Data += Now + "," + Price + ",(" + Price + "," + Price + ")" # If the last was the end of the day

            if re.search(r"\d+\.\d,\(\d+\.\d,\d+\.\d\)", Data) != None and Time >= 1430 and Time <= 1442: # If the last is lowest and it's the end of day
                Data += "," + Price + ";"

            elif float(re.sub(r"\)", "", Low_Wick)) > float(Price): # If the last was the start
                Data = re.sub(r"\d+\.\d\)", Price + ")", Data)

            elif float(re.sub(r"\(", "", High_Wick)) < float(Price): # If the last was the start
                Data = re.sub(r"\(\d+\.\d", "(" + Price, Data)

            Text += Data + "\n"
        else:
            Text += line if line != "" else None

    F.seek(0)

    if StartFollow == True:
        if re.search(Name +":", F.read()) == None:
            Text += Name + ":" + Now + "," + Price + ",(" + Price + "," + Price + ")" + "\n"

    F.close()

    F = open(path + "\\Stock\\{}".format(userid) +".txt", "w")
    F.write(Text)
    F.close()

    return "Success"

def get_StockInfo(source, StartFollow, userid): # Func. that gets information
    global Name
    global Price 

    soup = BeautifulSoup(source, "html.parser")
    Name = soup.find('span', {"data-attrid": 'Company Name'}).get_text()
    Price = soup.find('div', {"data-attrid": "Price"}).get_text()
    Price = re.search(r"[\d\s]+,\d", Price).group(0)
    Price = re.sub(r",", ".", Price)
    Price = re.sub(r"\s", "", Price)
    

    if StartFollow != None:
        write_Data(Name, Price, StartFollow, userid, False)
    #print(Price, Name)
    return Price

def parse(URL, StartFollow, userid): 
    global Price
    Html_script = get_Html(URL) # Writing Html Script in variable

    if Html_script.status_code == 200:
        #if Time >= 480 and Time < 840 and Follow == True:
            #print("Sorry Burse is closed...")
        #else:
        return get_StockInfo(Html_script.text, StartFollow, userid)

    else:
        print("Request failed\n" + str(Html_script))