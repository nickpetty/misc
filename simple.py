import json
import requests
import re

with open('config') as data_file:    
    userpass = json.load(data_file)

s = requests.Session()

signinURL = 'https://bank.simple.com/signin'
getGoalsURL = 'https://bank.simple.com/goals/data'
postGoalURL = 'https://bank.simple.com/goals/'

r = s.get(signinURL)
token = re.search('<meta name="_csrf" content="(.*)">', r.text).group(1)
data = {'username':userpass['username'], 'password':userpass['password'], '_csrf':token}


# Signin
r = s.post(signinURL, data=data)

goalData = {'amount':'30000', 'archived':'', 'color':'', 'contributed_amount':'10000', 'created':'', 
'finish':'', 'locked':'false', 'name':'house', 'paused':'', 'seq':0, 'start':'', 'uuid':'', 
'category':'', 'aprox_daily_contribution':0, 'target_amount':'30000'}

r = s.get(getGoalsURL)

goals = r.json()

r = s.post(postGoalURL, goalData)

print r.text




# i = 0
# while i < len(goals):
# 	if goals[i]['name'] == 'house':
# 		print goals[i]
# 		break
# 	else:
# 		i += 1


