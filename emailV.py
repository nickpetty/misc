import re
def isEmail(email):
	exp = re.compile(r'^[a-zA-Z0-9_.+-]+@[\w\.-]+\.[a-zA-Z]{2,3}$')
	if exp.match(email):
		return True
	else:
		return False

emails = {'nickpetty@gmail.com', 'nick&petty@gmail.com', 'nickpetty@gmai*l.co'}

for email in emails:
	if isEmail(email):
		print email + ' is valid.'
	else:
		print email + ' is not valid.'