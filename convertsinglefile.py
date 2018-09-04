import openpyxl
import csv

fileName='PMCtestfile.xlsx'

wb = openpyxl.load_workbook(fileName)
sh = wb.active
f = open(fileName+'converted2.csv', 'w')

c = csv.writer(f)
for r in sh.rows:
    c.writerow([cell.value for cell in r])
