# Created from https://bit.ly/2NyxdAG
from bs4 import BeautifulSoup
import requests
from requests.exceptions import ConnectionError
from requests_file import FileAdapter
import re
import argparse
import os

# Argument Parser
parser = argparse.ArgumentParser()
parser.add_argument( "url", type=str, help="The URL, either an http link or a file" )
args = parser.parse_args()
url=args.url

# Check if it's a file or an http link
if os.path.exists(args.url):
	# File exists, load it as a webpage
	url="file://"+os.path.realpath(args.url)
	s = requests.Session()
	s.mount('file://', FileAdapter())
	response = s.get(url)
elif url.find("http") == -1:
	# Not a file, check if it has http before we do an http request
	print( "ERROR: \"" + url + "\" is not a valid URL or a file" )
	quit()
else:
	# Try loading the URL, quit if it's not valid
	try:
		response = requests.get(url)
	except ConnectionError:
		print( "ERROR: \"" + url + "\" is not a valid URL or a file" )
		quit()

# Load the page with soup
soup = BeautifulSoup(response.text, 'lxml')

# Get all tables & figure out the largest table, that's likely to be the Full List
tables = soup.findChildren('table')
largestTable=0
largestTableSize=0
count=0
for table in tables:
	tableLen = len(table)
	#print(tableLen)
	if tableLen > largestTableSize:
		largestTableSize=tableLen
		largestTable=count
	count = count + 1

#print(largestTable, " ", largestTableSize)

# Iterate through all the rows in the table
rows = tables[largestTable].findChildren(['tr'])
for row in rows:
	cols = row.find_all('td')
	cols = [x.text.strip() for x in cols]
	if cols:
		print( cols[0], " - ", cols[2], " - ", cols[3] )

#for row in rows:
#	cells = row.findChildren('td')
#	for cell in cells:
#		value = cell.string
#		print( "The value in this cell is ", value)

quit()
imdb = []


# Store each item into dictionary (data), then put those into a list (imdb)
for index in range(0, len(movies)):
    # Seperate movie into: 'place', 'title', 'year'
    movie_string = movies[index].get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    movie_title = movie[len(str(index))+1:-7]
    year = re.search('\((.*?)\)', movie_string).group(1)
    place = movie[:len(str(index))-(len(movie))]
    data = {"movie_title": movie_title,
            "year": year,
            "place": place,
            "star_cast": crew[index],
            "rating": ratings[index],
            "vote": votes[index],
            "link": links[index]}
    imdb.append(data)

for item in imdb:
    print(item['place'], '-', item['movie_title'], '('+item['year']+') -', 'Starring:', item['star_cast'])

