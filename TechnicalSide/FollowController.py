import sqlite3
import datetime
import os
import Stocks_Parsing as SP 
import Currencies_Parsing as CP

conn = sqlite3.connect("People.db")
cursor = conn.cursor()
now = datetime.datetime.now()

def main():
	n = 1
	while n != 0:
		Sqlite_request(n)
		now = datetime.datetime.now()
		if now.month == "01" and now.day == "01":
			time.sleep(86400)
		n += 1

def Sqlite_request(id):
	cursor.execute("SELECT userid FROM Users WHERE id = ?;", (id,))
	Parse(cursor.fetchall()[0])

def Parse(userid):
	F = open(os.path.abspath(os.curdir) +"\\Name-Prices_Files\\Stock\\{}".format(userid[0]) +".txt", "r")
	if open(os.path.abspath(os.curdir) +"\\Name-Prices_Files\\Stock\\{}".format(userid[0]) +".txt", "r"):
		F.close()
		SP.write_Data(None, None, False, userid)
	#elif F = open(os.path.abspath(os.curdir) +"\\Name-Prices_Files\\Currency\\{}".format(userid[0]) +".txt", "r"):

	else:
		return
main()

