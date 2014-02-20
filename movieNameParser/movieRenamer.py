import re
import sys
import os
import commands

def stripJunk(*titles):
	for title in titles:
		print title
		results = re.compile(r'([uncut]?[extended]?\(?\[?\d{4}?.*(\.mp4|avi|mkv|mpg+))')
		matches = []
		for each in results.groups():
			matches.append(each)

		toStrip = str(matches[0])
		ext = str(matches[1])

		movieTitle = str(title).strip(toStrip).replace('.',' ').rstrip() + ext

		print movieTitle

def test(*titles):
	for title in titles:
		cmd = 'echo ' + str(title)
		print commands.getoutput(cmd)

stripJunk(sys.argv[1:])
#test(sys.argv[1:])