import sys
"""
Not my code found on/at https://blog.webnersolutions.com/split-large-csv-into-multiple-smaller-csv-files-with-python-script.
Splits csv into multiple files working
"""
fil='/Users/michaelingram/Downloads/MI_Petition_signers.csv'
csvfilename = open(fil, 'r').readlines()
file = 1

for j in range(len(csvfilename)):
		if j % 100000 == 0:
			open(str(fil[0:-4])+ str(file) + '.csv', 'w+').writelines(csvfilename[j:j+100000])
			file += 1
