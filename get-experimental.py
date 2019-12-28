#https://bit.ly/2NyxdAG
from bs4 import BeautifulSoup
import requests
import re

# Download IMDB's Top 250 data
url = 'https://250.took.nl/history/1996/4/26/full'
#url = 'https://250.took.nl/history/1996/11/19/full'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

#movies = soup.select('td.titleColumn')
#links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
#crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
#ratings = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=ir]')]
#votes = [b.attrs.get('data-value') for b in soup.select('td.ratingColumn strong')]

#print(soup.prettify())
#children = soup.find(class_="list-data")
#for child in children:
#  print(child)
tables = soup.findChildren('table')
#print(len(tables))
largestTable=0
largestTableSize=0
count=0
for table in tables:
	tableLen = len(table)
	print(tableLen)
	if tableLen > largestTableSize:
		largestTableSize=tableLen
		largestTable=count
	count = count + 1

print(largestTable, " ", largestTableSize)

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

