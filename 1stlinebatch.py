import csv
import os
import glob as gb
os.makedirs('lineadded2', exist_ok=True)

#filesNames=('/Users/michael/Documents/Geocodetest/workingcodes/*.csv')

for csvFilename in os.listdir('/Users/michael/Documents/Geocodetest/workingcodes'):
	if not csvFilename.endswith('.csv'):
		continue 
	print('Adding line to ' + csvFilename)
	

	csvRows=[]
	csvFileObj = open(csvFilename)
	readerObj = csv.reader(csvFileObj)
	for row in readerObj:
		#if readerObj.line_num == 1:
		#continue # skip first row
		csvRows.append(row)
	csvFileObj.close()


#write out CSV file

	csvFileObj = open(os.path.join('lineadded2',csvFilename),'w')
	csvwriter = csv.writer(csvFileObj)
	csvwriter.writerow(['1','4600 Silver Hill Rd','Suitland','MD','20746'])
	for row in csvRows:
		csvwriter.writerow(row+[])
		#row.append(row[4])
	csvFileObj.close()
