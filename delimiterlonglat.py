import csv
""" For geocoded resutls where lat and long are on columm. 
Splits into sepeate colums based on casenumber files from https://geocoding.geo.census.gov/"""

with open('splitfile.csv', 'r') as split_file:
	csv_reader = csv.reader(split_file, delimiter=',')
	
	with open('proccessd.csv', 'w') as f:
		csv_writer=csv.writer(f,quoting=csv.QUOTE_NONE,escapechar=' ')
		csv_writer.writerow(['Case number','Lat','Long'])
		for row in csv_reader:
			if row[3]== "Exact":				
				csv_writer.writerow([row[0],row[5]])
