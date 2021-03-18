import subprocess
import sys
import os
import csv
import glob
import pandas as pd
"""
Uses the csv created in locationprocessing.py
to access uscensus data through an API
created folders to stre geocoded results
combines files Then filtes columns by lat/long that have results and 
creates dataframe.
"""

folder='/Users/michael/Documents/pmc1416files'
if not (os.path.join(folder,'geocoded')):
	os.makedirs(os.path.join(folder,'/geocoded'))
else:
	print((os.path.join(folder,'geocoded'))+ ' already exist')

geocoded=((os.path.join(folder,'geocoded')))

#print(geocoded)
listofbash=open('/Users/michael/Documents/pmc1416files/pmc201416bashlist.csv')
csvreader = csv.reader(listofbash)


for row in csvreader:
	x=row[0].index('geocoded') #Determines the files names for checks#

	if os.path.exists(os.path.join(geocoded,row[0][x+9:])):
		print(row[0][(x+9):]+ ' has been created')
	
	else:
		print('creating ' +row[0][(x+9):])
		bashCommand =row[0]
		process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
		output, error = process.communicate()
		print(row[0] + ' has been created')
print('Geocoding complete')




os.chdir(geocoded)
doctitle='combineddoc'
extension = 'csv'


"""
combines the files created in locationprocessing.py
Then filtes columns by lat/long that have results and 
creates dataframe.
"""

all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#List of column headers to be added to each datafreame
columns=['chargeserialnumber','InputAddress','RangeMatch','TIGERMatchType','TIGEROutputAddress','Longitude/Latitude','TIGERLineID','TIGERLineIDSide']

#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f,names = columns) for f in all_filenames ])
#print(combined_csv)

#export to csv utf-8-sig
joins=folder,doctitle,
combined_csv.to_csv(os.path.join(*joins)+'.csv', index=False)


df=pd.read_csv((os.path.join(*joins))+'.csv')

#determines header list of combinedlist datagrame
headerlist=list(df)
print(headerlist[0])
print(headerlist[5])

"""
Splits dataframe row[5] and reassinges new splits to columns ttitles
New columns splits are put into newframe and newframe is filtered by latitude
dataframe out put to csv
"""
tf=df[headerlist[5]].str.split(',',expand=True)
df['latitude'] = tf[1]
df['longitude'] = tf[0]
df['chargeserialnumber']=df[headerlist[0]]
newframe=df.filter(['chargeserialnumber','latitude','longitude'],axis=1)
df=newframe[~newframe['latitude'].isnull()]

#Resulting dataframe is made into csv
df.to_csv('/Users/michael/Documents/pmc1416files/uploadready20190612.csv',index=False)
