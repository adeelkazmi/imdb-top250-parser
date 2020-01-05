# Generates a one line CSV output of the top IMDb movies from arg1
 
from bs4 import BeautifulSoup
import check_url

import os

# Check if the MAX_FILMS environment variable is set and use it
filmsToCollect = int( os.environ.get( 'MAX_FILMS', '251' ) )

# Load the page with soup
soup = BeautifulSoup(check_url.response.text, 'lxml')

# Get all tables & figure out the largest table, that's likely to be the Full List
tables = soup.findChildren('table')
largestTable=0
largestTableSize=0
count=0
for table in tables:
	tableLen = len(table)
	if tableLen > largestTableSize:
		largestTableSize=tableLen
		largestTable=count
	count = count + 1

# Iterate through all the rows in the table
fullStr=""
rows = tables[largestTable].findChildren(['tr'])
rowsCollected=0
for row in rows:
	cols = row.find_all('td')
	cols = [x.text.strip() for x in cols]
	if cols:
		fullStr=fullStr + cols[3].replace(',','') + ","
		rowsCollected = rowsCollected + 1
		if rowsCollected >= filmsToCollect:
			break

print( fullStr )

