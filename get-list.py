# Created from https://bit.ly/2NyxdAG
from bs4 import BeautifulSoup
import check_url

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
rows = tables[largestTable].findChildren(['tr'])
for row in rows:
	cols = row.find_all('td')
	cols = [x.text.strip() for x in cols]
	if cols:
		print( cols[0], " - ", cols[2], " - ", cols[3] )

