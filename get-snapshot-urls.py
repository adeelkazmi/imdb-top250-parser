# Retrieve all the URL snapshots from https://250.took.nl
from bs4 import BeautifulSoup
import requests

urlBase = 'https://250.took.nl'
urlSuffix = '/full'
firstSnapshot = '/history/2019/12/2'

nextSnapshot = firstSnapshot
#for x in range(100):
while nextSnapshot:
	url = urlBase + nextSnapshot + urlSuffix
	print(url)
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'lxml')
	nextDiv = soup.find(class_="compare-next")
	if not nextDiv:
		break
	children = nextDiv.findChildren(['a'])
	if not children:
		break
	nextSnapshot = children[0].get('href')
