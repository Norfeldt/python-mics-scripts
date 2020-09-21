from glob import glob
from datetime import datetime
nowStr = datetime.now().strftime('%Y-%m-%d %H.%M.%S')

replaceCommaByDot = True
replaceSemiByComma = True
convertPrefix = 'EnCSV '

singleFile = True


for csvFile in glob('*.csv'):
	if convertPrefix in csvFile:
		continue
		
	content = []
	with open(csvFile,'r') as DAfile:
		content = DAfile.readlines()
		
	with open(convertPrefix + csvFile, 'w') as ENfile:
		for line in content:
			line = line.replace(',', '.') if replaceCommaByDot else line
			line = line.replace(';', ',') if replaceSemiByComma else line			
			ENfile.write( line )

if singleFile:
	content = []			
	for csvFile in glob('*.csv'):
		if convertPrefix not in csvFile:
			continue
		with open(csvFile,'r') as DAfile:
			content += DAfile.readlines()
	
	singleFileName = 'DATA ' + nowStr + '.csv'	
	with open(singleFileName,'w') as sFile:
		for line in content:
			sFile.write( line )
