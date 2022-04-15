from sqlite3.test.factory import MyCursor
import mysql.connector

#Created database
#set host to the localhost on the computer
#the databases username was set to root
#password was set to 12345678
#a database was created initially with the name "mydatabase"

mydb = mysql.connector.connect(
host="localhost",
username="root",
password="12345678",
database="mydatabase"
)
mycursor = mydb.cursor()

'''
TEST
THESE ARE ALL TEST CASES THAT WERE USED TO UNDERSTAND THE MYSQL DATABASE BETTER
TEST
'''








'''mycursor.execute("SELECT COUNT(*) FROM animals")
numResult = mycursor
if numResult == 0:
	mycursor.execute("CREATE TABLE animals (name VARCHAR(255), species VARCHAR(255))")'''

'creates the database'

'mycursor.execute("CREATE DATABASE mydatabase")'

'shows databases'
'''mycursor.execute("SHOW DATABASES")
for x in mycursor:
	print(x)
	if "mydatabase" in mycursor:
		print("database is created")'''
	
'prints databases'
'''mycursor.execute("SHOW TABLES")
for x in mycursor:
	print(x)'''
	
'''mycursor.execute("SHOW COLUMNS FROM animals")
for x in mycursor:
	print(x)'''
	
'''mycursor.execute("SELECT * FROM animals")
for i in mycursor:
	print(i)'''
	
	
	
	
	
	
#While loop that will continuously ask the user to select one of the options below
#The loop will only break if the user selects "4" which will break the loop
while(True):
	print("-----------------")
	print("1 - input database")
	print("2 - read database")
	print("3 - delete database")
	print("4 - exit")
	print("-----------------")
	
	#userinput only accepts an integer blocking sql injection
	userInput = int(input())
	
	#breaks loop for a 4 entered or anything greater than 4 or less than 1
	if userInput == 4:
		break
	elif (userInput > 4) or (userInput < 1):
		break
	
	#Inserts an entry into the database accepting the animal's name and species stored together
	if userInput == 1:
		#sql instruction here that will insert the name and species
		sql = ("INSERT INTO animals (name, species) VALUES (%s, %s)")
		#accepts the animal name input
		animal = input("What is the name of the animal:")
		#accepts the animal species input
		species = input("What is the species of the animal:")
		#stores the values into val which will then execute the sql statement with val inserted in
		val = (animal, species)
		mycursor.execute(sql, val)
		mydb.commit()
		#prints the count of the rows and tells the user the rows inserted.
		print(mycursor.rowcount, "record(s) inserted.")
		
	#reads the database entries to the user
	if userInput == 2:
		#prints all entries with this sql statement
		mycursor.execute("SELECT * FROM animals")
		myresult = mycursor.fetchall()
		for x in myresult:
			print(x)
	
	#deletes all entries from the database
	#then tells the user the number of rows deleted
	if userInput == 3:
		mycursor.execute("DELETE FROM animals")
		mydb.commit()
		print(mycursor.rowcount, "record(s) deleted")