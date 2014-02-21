import re
from urllib2 import Request, urlopen
import urllib

def downloadPoster(movieName):
	apiKey = '<apiKey>'
	imgBaseURL = "http://image.tmdb.org/t/p/w500/" # URL to be merged with poster_path
	movie = movieName.replace(' ','+').replace('-', "%2D").replace("'", '%27').replace("&", "%26") # Make movieName HTTP friendly
	url = "http://api.themoviedb.org/3/search/movie?query=" + movie + '&' + apiKey 
	
	print 'Downloading ' + movieName

	request = Request(url)
	result = urlopen(request).read()

	check = re.compile(r'results":(\[\])') # Check if movie found

	if not check.search(result):
		match = re.compile(r'poster_path":"/([\w\d]*\.jpg)') # Find poster_path in JSON
		posterURL = match.split(result)[1] # Pull poster url from JSON
		url1 = imgBaseURL + posterURL + '?' + apiKey # Create URL for poster
		saveName = movieName + '.jpg' # Generate IMG name
		urllib.urlretrieve(url1, 'posters/' + saveName) # Save image
	else:
		print movieName + ' not found.'

mList = open('movieList.txt', 'r') # Open movieList.txt
for movie in mList.readlines():
	if "srt" not in movie:
		if "mp4" or "avi" or "mkv" or "mpg" in movie:
			toStrip = re.compile(r'([uncut]?[extended]?\(?\[?\d{4}?.*(mp4|avi|mkv|mpg+))', re.I) # Strip out 'date', 'extended', 'unrated', misc info, and extension.	
			movie = toStrip.split(movie)[0].replace('.',' ').strip('[\n,mp4,avi,mkv,mpg]').rstrip()
			downloadPoster(movie)
