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

