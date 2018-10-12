import subprocess
import sys
import os
import csv

listofbash=open('/Users/michael/Documents/pmc1417files/results/bashlist1417.csv') #files to be ran through command loop
csvreader = csv.reader(listofbash)


for row in csvreader:
	x=row[0].index('geocoded/') #Determines the files names for checks#
	print(row[0][(x+9):]) #Confirms file names for  
	
	if os.path.exists('/Users/michael/Documents/pmc1417files/results/geocoded/'+row[0][x+9:]):
		print(row[0][(x+9):]+ ' has been created')
	else:
		print('creating ' +row[0][(x+9):])
		bashCommand =row[0]
		process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
		output, error = process.communicate()
		print(row[0][(x+9):] + ' has been done')
	

print('Geocoding complete')
