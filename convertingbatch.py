import openpyxl
import os
import csv

excelFiles=os.listdir('/Users/michael/Documents/Geocodetest')
for filenames in excelFiles:
	if filenames.endswith('xlsx'):
		wb=openpyxl.load_workbook(filenames)
		sh = wb.active
		f = open(filenames[0:-5]+'convertedbatch.csv', 'w',encoding='utf-8-sig')

		filewriter = csv.writer(f)
		for p in sh.rows:
   			filewriter.writerow([cell.value for cell in p])
		print (filenames + ' has been converted.')
		

