#!/usr/bin/env python3.6

import sys
import mysql.connector 

LOG3 = sys.stdin.readline()
LOG2 = LOG3.replace("(", "")
LOG1 = LOG2.replace(")", "")
#LOG2 = LOG[15:None]
LOG = LOG1.split()
#STR = str(LOG[17:])
STR = " ".join(LOG[16:])

#testfile = ('/home/centos/bash/tasks-month2/temp-logs/Exercise4_output')

file=open(r"/home/centos/bash/tasks-month2/temp-logs/Exercise4_output","a")
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
#file.write(str(LOG[17:])


file.close()

db = mysql.connector.connect(
    user="root",
    password="abc123",
    database="Syslog_Data"
)

cursor = db.cursor()

sql = ("INSERT INTO Exercise4 "
	"(Date, Time, Server_IP, Source_IP, Client_ID, Http_Method, Requested_path, Http_protocol, Status_code, Size_of_object, Users_data) "
	"VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
val = (LOG[6], LOG[7], LOG[8], LOG[9], LOG[4], LOG[10], LOG[11], LOG[12], LOG[13], LOG[14], STR)
cursor.execute(sql, val)

db.commit()
cursor.close()
db.close()
