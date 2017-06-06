import sqlite3
import sys


def printDB():

	try:
		result = theCursor.execute("SELECT ID, FName, LName, Age, Address, Salary, HireDate FROM Employees")

		for row in result:
			print(row[0])
			print(row[1])
			print(row[2])
			print(row[3])
			print(row[4])
			print(row[5])
			print(row[6])
			

	except sqlite3.OperationalError:
		print("Table Doesn't Exist")

	except:
		print("Could Find Database")

db_conn = sqlite3.connect("test.db")

print("Database Created")

db_conn.execute("DROP TABLE IF EXISTS Employees")
db_conn.commit()

theCursor = db_conn.cursor()
try:
	db_conn.execute("CREATE TABLE Employees(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, FName TEXT NOT NULL, LName TEXT NOT NULL, AGE INTEGER NOT NULL, Address TEXT, Salary REAL, HireDate TEXT);")

	db_conn.commit()
except sqlite3.OperationalError:
	print("Table couldn't be created")

print("Table Create")

db_conn.execute("INSERT INTO Employees (FName, LName, Age, Address, Salary, HireDate) VALUES ('Derek', 'Banas', 41, '123 Main St', 500000,date('now'))")
db_conn.commit()

printDB()

db_conn.close()

print("Database Closed")