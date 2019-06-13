#!/usr/bin/env python3
import csv
import sys
import os
import shutil
import subprocess
from subprocess import Popen, PIPE, STDOUT

"""
Formats the files to be able to processed by the us geocode 
website service
Seperates files into 1000 records 

Creates a formated list of fiedls to be geoced throught desktops
Curl command from terminal

Developed on OSX not tested on any windows machine

"""
#processes files to add in missing information 

#File to be processed

file='/Users/michael/Documents/pmc1416files/pmc201416needtogeocode.csv'
togeocode=file.find('needtogeocode.csv')
dirname=os.path.dirname(file)
processedfile=file[:togeocode]+'processed.csv'
city='Phoenix' #city where geocoding address 
state='AZ' #State where geocoding address


if os.path.isfile(processedfile):
	print(processedfile + ' has been created')
else:
		with open(file,'r') as l:
			locationfile=csv.reader(l)
			with open(processedfile, 'w') as w:
				for row in locationfile:
					writefile=csv.writer(w)
					writefile.writerow([row[2],row[14],city,state,' '])
			print('File Processed')

"""
Section will contain cleaning procedure once cleaning.py has been completed

"""


#Creates split subdirectory
fil=processedfile

csvfilename = open(fil, 'r').readlines()
#Checks to see if directory exist
if os.path.exists(os.path.join((os.path.join(dirname,'split')))):
	print(os.path.join((os.path.join(dirname,'split')))+' already exists')
else:
	(os.makedirs((os.path.join((os.path.join(dirname,'split'))))))
	print(os.path.join((os.path.join(dirname,'split')))+' created')

splitdirectory=(os.path.join((os.path.join(dirname,'split'))))
#Seperates the processed file into files with x(1000) records per file
#Sepearted files in file dir/split

number = 1
x=1000

for j in range(len(csvfilename)):
		if j % x == 0:
			open(str(fil[0:-4])+ str(number) + '.csv', 'w+').writelines(csvfilename[j:j+x])
			shutil.move(str(fil[0:-4])+ str(number) + '.csv',splitdirectory,)
			number+= 1
print('Files split')


#Creates the baslist to be used in the commandloop program

dirpath=os.path.dirname(file)

#os.makedirs=os.path.join(dirpath,'geocoded')
resultstpath=os.path.join(dirpath,'geocoded')  

if not os.path.exists(resultstpath):
    os.makedirs(os.path.join(dirpath,'geocoded'))
    print("Directory " , resultstpath ,  " Created ")
else:    
    print("Directory " , resultstpath ,  " already exists")



with open (os.path.join(os.path.dirname(file),file[:togeocode]+'bashlist.csv'), 'w') as bashfile:
	bashwriter=csv.writer(bashfile, delimiter=',')

	for csvFilename in os.listdir(splitdirectory):
		processedlocation=csvFilename.find('processed')
		filenumber=processedlocation+9
		sourcefile=(os.path.join(splitdirectory,csvFilename))
		outputfile=(os.path.join(resultstpath,((csvFilename[:processedlocation]+'_'+csvFilename[filenumber:-4]+'results.csv'))))
		bashwriter.writerow(['curl --form addressFile=@'+sourcefile+
			' --form benchmark=9 https://geocoding.geo.census.gov/geocoder/locations/addressbatch' 
			' --output '+outputfile])
print('Bash list Created')
