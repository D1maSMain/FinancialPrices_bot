import requests # For Http requests
import sqlite3 # For working with SQLite database
from bs4 import BeautifulSoup # For working with Html Script
import re # For regex
import os
import fileinput
from datetime import datetime

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
           'accept': '*/*'} # Using headers

User = "" # Current User
Name = "" # Global Currency Name
Price = "" # Global Price

Time = datetime.now().hour*60 + datetime.now().minute

def get_Html(url, params = None): # Func. that returns script
    result = requests.get(url, headers=HEADERS, params=params) # Making Http request
    return result

def write_Data(Name, Price,StartFollow, userid):
    global Time

    DateTimeFormat = "%Y/%m/%d-%H:%M"
    Now = datetime.now().strftime(DateTimeFormat) # Making value with date
    
    F = open(os.path.abspath(os.curdir) +"\\TechnicalSide\\Name-Prices_Files\\Currency\\{}".format(userid) +".txt", "w+") # Making file | Check it made

    F.close()

    F = open(os.path.abspath(os.curdir) +"\\TechnicalSide\\Name-Prices_Files\\Currency\\{}".format(userid) +".txt", "r") # Open for reading

    Text = "" # Whole text in file

    for line in F: # Walking on the lines in file
        if re.match(".+:.+", line) != None:

            Data = re.match(".+:.+", line).group(0)

            if StartFollow == None:
                print("https://www.google.com/search?q=" + re.search("[\w\s]+\:", Data).group(0))
                Price = parse("https://www.google.com/search?q=" + re.search("[\w\s]+\:", Data).group(0) + "+price", None, None)

            elif re.search("\w+\:", Data).group(0) == Name + ":" and StartFollow == True:
                print("Exist")
                return

            elif re.search("\w+\:", Data).group(0) == Name + ":" and StartFollow == False:
                Text += ""
                continue
            
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

            Text += Data + "\n"
        else:
            Text += line if line != "" else None
    F.seek(0)

    if StartFollow == True:
        if re.search(Name +":", F.read()) == None:
            Text += "\n" + Name + ":" + Now + "," + Price + ",(" + Price + "," + Price + ")" + "\n"

    F.close()

    F = open(os.path.abspath(os.curdir) +"\\TechnicalSide\\Name-Prices_Files\\Currency\\{}".format(userid) +".txt", "w")
    F.write(Text)
    F.close()

    return "Success"

def get_CurrencyInfo(source, StartFollow, userid): # Func. that gets information
    global Name
    global Price 

    soup = BeautifulSoup(source.text, "html.parser")
    Price = soup.find('div', {"id": "knowledge-currency__updatable-data-column"}).get_text()
    Price = re.search(r"\d+,\d", Price).group(0)
    Price = re.sub(",", ".", Price)

    if StartFollow == True:
        write_Data(Name, Price, StartFollow, userid)
    print(Price, Name)
    return Price

def parse(URL, StartFollow, userid, Currency): # 1.1 сек. (при том что запущен Spotify, Chrome, работает Bluetooth) нужно - 200 мсек. (Уменьшить в 5 раз)
    global Price
    global Name
    
    Html_script = get_Html(URL) # Writing Html Script in variable
    Name = Currency

    if Html_script.status_code == 200:
        #if Time >= 480 and Time < 840 and Follow == True:
            #print("Sorry Burse is closed...")
        #else:
        return get_CurrencyInfo(Html_script, StartFollow, userid)
    else:
        print("Request failed")

