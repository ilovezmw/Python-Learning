#!/usr/bin/python

import sys
import ftplib
import os


#server = "10.44.0.42"
#user = "visitor"
#password = "P@ssw0rd"
#source = "/Downloads"
#destination = "C:/temp"
#interval = 0.05

ftp = ftplib.FTP() 

FTPIP= "10.44.0.42"
FTPPORT= 21
USERNAME= "visitor"
USERPWD= "P@ssw0rd"
ftp.connect(FTPIP,FTPPORT) 
ftp.login(USERNAME,USERPWD) 
ftp.set_pasv(0)
CURRTPATH= "/Downloads"
ftp.cwd(CURRTPATH) 
DownLocalFilename="C:/temp/test1.txt"
f = open(DownLocalFilename,'wb') 
DownRoteFilename="test2.txt"
ftp.retrbinary('RETR ' + DownRoteFilename , f.write ,1024) 
f.close() 
ftp.close()