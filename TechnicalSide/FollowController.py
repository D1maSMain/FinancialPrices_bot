import sqlite3
import datetime
import os
import Stocks_Parsing as SP
import Currencies_Parsing as CP


now = datetime.datetime.now()
n = 0

conn = sqlite3.connect('People.db')
cur = conn.cursor()

def main(connection, cursor):
	global n

	n = 1
	while n != -1:
		Sqlite_request(cursor, n)
		now = datetime.datetime.now()
		if now.month == "01" and now.day == "01":
			time.sleep(1440*60)
		n+=1

def Sqlite_request(cursor, id):
	global n

	cursor.execute("SELECT userid FROM Users WHERE id = ?;", (id,))
	print(id)
	try:
		CallWrite(cursor.fetchall()[0][0])
		return
	except:
		n = 0
		print("except1")
		return

def CallWrite(userid):
	try: 
		open(os.path.abspath(os.curdir) +"\\Name-Prices_Files\\Stock\\{}".format(userid) +".txt", "r")
		print(SP.write_Data(None, None, None, userid, True))
	except:
		print("pass")

	try:
		open(os.path.abspath(os.curdir) +"\\Name-Prices_Files\\Currency\\{}".format(userid) +".txt", "r")
		CP.write_Data(None, None, None, userid)
		return
	except:
		return
main(conn, cur)
