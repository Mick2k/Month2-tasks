#!/usr/bin/env python3.6

#import modules - sys for reading the input and also a mysql connecting mod
import sys
import mysql.connector 

##START OF PARSING DATA.
#used a few variables to remove the parentheses from my input (.replace).
#the input was created as a list to call each word by an index utilising .split feature.
# 'STR' used the .join feature to pull all the 'Users_agent' data into 1 index from a range.
LOG3 = sys.stdin.readline()
LOG2 = LOG3.replace("(", "")
LOG1 = LOG2.replace(")", "")
LOG = LOG1.split()
STR = " ".join(LOG[16:])

#START OF A STRUCTURED LOG FILE.
#opens, reads and amends data in file.
file=open(r"/home/centos/bash/tasks-month2/temp-logs/Exercise4_output","a")
#writes a newline before continuing writing each heading followed by the relevent list index.
file.write(" \n")
file.write("Date: " + LOG[6] + "\n")
file.write("Time: " + LOG[7] + "\n")
file.write("Server IP: " + LOG[8] + "\n")
file.write("Source IP: " + LOG[9] + "\n")
file.write("Client ID: " + LOG[4] + "\n")
file.write("HTTP Method: " + LOG[10] + "\n")
file.write("Path: " + LOG[11] + "\n")
file.write("HTTP protocol: " + LOG[12] + "\n")
file.write("Status code: " + LOG[13] + "\n")
file.write("Size of object: " + LOG[14] + "\n")
file.write("Users agent: " + STR + "\n")
#closes and saves the file.
file.close()




#START OF DB ENTRY
#connects to MySQL database
db = mysql.connector.connect(
    user="root",
    password="******", #removed cleartext password before uploading to GitHub.
    database="Syslog_Data"
)

#db.cursor() is required to handle entries (and other MySQL commands) into DB.
cursor = db.cursor()

#Variables used to state the DB fields followed by values in variable form, pulling this data from the LIST inputed at the beginning.
sql = ("INSERT INTO Exercise4 "
	"(Date, Time, Server_IP, Source_IP, Client_ID, Http_Method, Requested_path, Http_protocol, Status_code, Size_of_object, Users_data) "
	"VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
val = (LOG[6], LOG[7], LOG[8], LOG[9], LOG[4], LOG[10], LOG[11], LOG[12], LOG[13], LOG[14], STR)

#used to execute the commands in the stated variables.
cursor.execute(sql, val)

#saves data.
db.commit()
#closes the used previously (frees up server resources).
cursor.close()
#closes DB.
db.close()
