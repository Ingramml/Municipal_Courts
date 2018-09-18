import subprocess
import sys
import os
import csv
"""
Loops through created CSV to launch command line bash command uplading file to US geocders.

"""

listofbash=open('/Users/michael/Documents/pmc1417files/bashlist.csv')
csvreader = csv.reader(listofbash)

for row in csvreader:
	if os.path.exists('/Users/michael/Documents/pmc1417files/results/'+row[0][223:]):
		print(row[0][-27:]+ ' has been created')
	else:
		print('creating ' +row[0][223:])
		bashCommand = row[0]
		process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
		output, error = process.communicate()
		print(row[0][223:] + ' has been done')
	

print('Geocoding complete')
