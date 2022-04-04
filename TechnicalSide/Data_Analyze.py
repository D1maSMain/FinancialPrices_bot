import datetime

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
import os
import re
from matplotlib.dates import MONDAY, DateFormatter, DayLocator, WeekdayLocator
import fileinput

from mpl_finance import candlestick_ohlc

Name = "3M"
Index = "1"

data = pd.DataFrame(columns = ["Time", "Open", "High", "Low", "Close"])

F = open(os.path.abspath(os.curdir) +"\\Name-Prices_Files\\" + str(Index) + ".txt", "r")

end = False
daycounter = 0
datemin = ""

for line in F:
    if re.search(Name + ":.+", line) != None:
        Data =  re.search(Name + ":.+", line).group(0)

        while end == False:
            if re.search(r"\d+\.\d;", Data) != None:
                daycounter += 1

                Time = re.search(r"\d+/\d{2}/\d{2}-\d{2}:\d{2}", Data).group(0)
                Open = re.search(r"[^\(]\d+\.\d[^;\)]", Data).group(0)
                High = re.search(r"\(\d+\.\d", Data).group(0)
                Low = re.search(r"\d+\.\d\)", Data).group(0)
                Close = re.search(r"\d+\.\d;", Data).group(0)

                High = re.sub(r"\(", "\\(", High)
                Low = re.sub(r"\)", "\\)", Low)
                Data = re.sub(Time, "", Data)
                Data = re.sub(Open, "", Data)
                Data = re.sub(High, "", Data)
                Data = re.sub(Low, "", Data)
                Data = re.sub(Close, "", Data)
                High = re.sub(r"\\\(", "", High)
                Low = re.sub(r"\\\)", "", Low)

                Open = re.sub(",", "", Open)
                Close = re.sub(";", "", Close)

                Open = float(Open)
                High = float(High)
                Low = float(Low)
                Close = float(Close)

                data = data.append({"Time": Time, "Open": Open, "High": High, "Low": Low, "Close": Close}, ignore_index = True)

                if daycounter == 1:
                    datemin = Time

            else:
                end = True


F.close()

data["Time"] = pd.to_datetime(data["Time"], errors = 'raise', format = "%Y/%m/%d-%H:%M")
datemin = pd.to_datetime(datemin, errors = 'raise', format = "%Y/%m/%d-%H:%M")

mondays = WeekdayLocator(MONDAY)      
alldays = DayLocator()              
weekFormatter = DateFormatter('%b %d')
dayFormatter = DateFormatter('%d')

data = data[(data["Time"] >= data["Time"].iloc[0]) & (data["Time"] <= data["Time"].iloc[len(data)-1])]

fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2)
ax.xaxis.set_major_locator(mondays)
ax.xaxis.set_minor_locator(alldays)
ax.xaxis.set_major_formatter(weekFormatter)
ax.xaxis.set_minor_formatter(dayFormatter)

candlestick_ohlc(ax, zip(mdates.date2num(data["Time"]),
                         data['Open'], data['High'],
                         data['Low'], data['Close']), width=0.5, colorup='#53c156', colordown='#ff1717')
ax.xaxis_date()
ax.autoscale_view()
ax.set_xlim(mdates.date2num(datemin) - 1, mdates.date2num(datemin) + 15)
plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')

fig.savefig(''+os.path.abspath(os.curdir)+'\\Temp\\'+ Name +'.png', bbox_inches='tight')
plt.show()

plt.close(fig)