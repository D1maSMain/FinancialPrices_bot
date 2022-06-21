import datetime

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
import os
import re
from matplotlib.dates import MONDAY, DateFormatter, DayLocator, WeekdayLocator
import fileinput

from mpl_finance import candlestick_ohlc


def GetData(Name, U_id, dataStart):

    data = pd.DataFrame(columns = ["Time", "Open", "High", "Low", "Close"])

    F = open(os.path.abspath(os.curdir) +"\\TechnicalSide\\Name-Prices_Files\\Stock\\" + str(U_id) + ".txt", "r")

    end = False
    daycounter = 0
    StartRecord = False
    datemin = ""
    print(dataStart)

    for line in F:
        if re.search(Name + ":.+", line) != None:
            Data = re.search(Name + ":.+", line).group(0)

            while end == False:
                
                if re.search(r"\d+\.\d;", Data) != None and daycounter <= 16:

                    Time = re.search(r"\d+/\d{2}/\d{2}-\d{2}:\d{2}", Data).group(0)
                    if re.search(dataStart, Time) != None and daycounter == 0:
                        StartRecord = True
                        print(StartRecord)
                    Open = re.search(r"[^\(]\d+\.\d[^;\)]", Data).group(0)
                    High = re.search(r"\(\d+\.\d,", Data).group(0)
                    Low = re.search(r"\d+\.\d\)", Data).group(0)
                    Close = re.search(r",\d+\.\d;", Data).group(0)

                    High = re.sub(r"\(", "\\(", High)
                    Low = re.sub(r"\)", "\\)", Low)
                    Day = Time+Open+High+Low+Close
                    print(Day)
                    Data = re.sub(Day, "", Data)
                    print(Data)
                    High = re.sub(r"\\\(", "", High)
                    Low = re.sub(r"\\\)", "", Low)

                    Open = re.sub(",", "", Open)
                    High = re.sub(",", "", High)
                    Close = re.sub("[;,]", "", Close)

                    if StartRecord == True:
                        daycounter += 1
                        Open = float(Open)
                        High = float(High)
                        Low = float(Low)
                        Close = float(Close)

                        data = data.append({"Time": Time, "Open": Open, "High": High, "Low": Low, "Close": Close}, ignore_index = True)

                        if daycounter == 1:
                            datemin = Time
                            print(datemin)
                            print(data)

                else:
                    if daycounter == 0:
                        return "WrongDate"
                    end = True

    F.close()

    data["Time"] = pd.to_datetime(data["Time"], errors = 'raise', format = "%Y/%m/%d-%H:%M")
    datemin = pd.to_datetime(datemin, errors = 'raise', format = "%Y/%m/%d-%H:%M")

    Dates = [data["Time"], datemin]
    print(data)
    return DrawGraph(data, datemin, Name)


def DrawGraph(data, datemin, Name):
    Months = mdates.MonthLocator()      
    alldays = DayLocator()              
    weekFormatter = DateFormatter('%b %d')
    dayFormatter = DateFormatter('%d')

    data = data[(data["Time"] >= data["Time"].iloc[0]) & (data["Time"] <= data["Time"].iloc[len(data)-1])]

    fig, ax = plt.subplots()
    fig.subplots_adjust(bottom=0.2)
    ax.xaxis.set_major_locator(Months)
    ax.xaxis.set_minor_locator(alldays)
    ax.xaxis.set_major_formatter(weekFormatter)
    ax.xaxis.set_minor_formatter(dayFormatter)

    candlestick_ohlc(ax, zip(mdates.date2num(data["Time"]),
                            data['Open'], data['High'],
                            data['Low'], data['Close']), width=0.5, colorup='#53c156', colordown='#ff1717')
    ax.xaxis_date()
    ax.autoscale_view()
    ax.set_xlim(mdates.date2num(datemin), mdates.date2num(datemin) + 15)
    plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')

    lastArg = len(data["Time"])-1
    path = os.path.abspath(os.curdir)+'\\TechnicalSide\\Temp\\'+re.sub("[\s:]", "-", Name+"_"+str(datemin)+"#"+str(data.iloc[lastArg, 0])+'.png')
    fig.savefig(path, bbox_inches='tight')

    plt.close(fig)
    return path