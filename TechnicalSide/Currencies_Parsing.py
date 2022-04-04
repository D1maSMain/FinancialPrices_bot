import requests # For Http requests
import sqlite3 # For working with SQLite database
from bs4 import BeautifulSoup # For working with Html Script
import re # For regexs
import os
import fileinput
from datetime import datetime

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
           'accept': '*/*'} # Using headers

Follow = False # True - False
User = "" # Current User
Name = "" # Global Name
Price = "" # Global Price

Time = datetime.now().hour*60 + datetime.now().minute

def get_Html(url, params = None): # Func. that returns script
    result = requests.get(url, headers=HEADERS, params=params) # Making Http request
    return result

def write_Data(Name, Price):
    global Time

    conn = sqlite3.connect("People.db")
    cursor = conn.cursor()

    cursor.execute("SELECT userid FROM Users WHERE username=?", ("Dimas",)) # Getting User_Id
    id = cursor.fetchall()[0]

    DateTimeFormat = "%Y/%m/%d-%H:%M"
    Now = datetime.now().strftime(DateTimeFormat) # Making value with date
    
    F = open(os.path.abspath(os.curdir) +"\\Name-Prices_Files\\Currency\\{}".format(id[0]) +".txt", "a+") # Making file | Check it made

    F.close()

    F = open(os.path.abspath(os.curdir) +"\\Name-Prices_Files\\Currency\\{}".format(id[0]) +".txt", "r") # Open for reading

    Text = "" # Whole text in file

    for line in F: # Walking on the lines in file
        if re.match(Name +":.+", line) != None:

            Data = re.match(Name +":.+", line).group(0)
            High_Wick = re.search(r"\(\d+\.\d", Data).group(0)
            Low_Wick = re.search(r"\d+\.\d\)", Data).group(0)

            if Data[-1] == ";":
                Data += Now + "," + Price + ",(" + Price + "," + Price + ")" # If the last was the end of the day

            if re.search(r"\d+\.\d,\(\d+\.\d,\d+\.\d\)", Data) and Time >= 1430 and Time < 1439 != None: # If the last is lowest and it's the end of day
                Data += "," + Price + ";"

            elif float(re.sub(r"\)", "", Low_Wick)) > float(Price): # If the last was the start
                Data = re.sub(r"\d+\.\d\)", Price + ")", Data) + "\n"

            elif float(re.sub(r"\(", "", High_Wick)) < float(Price): # If the last was the start
                Data = re.sub(r"\(\d+\.\d", "(" + Price, Data) + "\n"

            Text += Data
        else:
            Text += line if line != "" else None
    F.seek(0)

    if re.search(Name +":", F.read()) == None:
        Text += "\n" + Name + ":" + Now + "," + Price

    F.close()

    F = open(os.path.abspath(os.curdir) +"\\Name-Prices_Files\\Currency\\{}".format(id[0]) +".txt", "w")
    F.write(Text)
    F.close()

def get_CurrencyInfo(source): # Func. that gets information
    global Name
    global Price 

    soup = BeautifulSoup(source.text, "html.parser")
    Price = soup.find('div', {"id": "knowledge-currency__updatable-data-column"}).get_text()
    Price = re.search(r"\d+,\d", Price).group(0)
    Price = re.sub(",", ".", Price)

    if Follow == True:
        write_Data(Name, Price)
    else:
        print(Price)

def parse(URL): # 1.1 сек. (при том что запущен Spotify, Chrome, работает Bluetooth) нужно - 200 мсек. (Уменьшить в 5 раз)
    global Price
    Html_script = get_Html(URL) # Writing Html Script in variable

    if Html_script.status_code == 200:
        #if Time >= 480 and Time < 840 and Follow == True:
            #print("Sorry Burse is closed...")
        #else:
        get_CurrencyInfo(Html_script)
        
        return Price
    else:
        print("Request failed")
