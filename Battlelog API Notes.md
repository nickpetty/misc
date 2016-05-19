Battlelog API Notes
-------------------

Required headers (for all post/get):

	+ Origin:http://battlelog.battlefield.com


A ping interface is available on localhost:3215 (POST)

	+ /ping/gameservers
	+ ?ipAddrList= <ip's seperated by commas>
	  + Seems only ip's of bf4 servers return a valid response


Response:

`[ {"ip":"192.223.29.40","time":17}, {"ip":"74.91.124.229","time":42} ]`


Comcenter info (users/friends):

	+ (GET) http://battlelog.battlefield.com/bf4/comcenter/checkIdle/
	+ (GET) http://battlelog.battlefield.com/bf4/comcenter/setActive/
	+ (GET) http://battlelog.battlefield.com/bf4/comcenter/initComcenter


Game status:

	+ http://127.0.0.1:3215/game/status?masterTitleId=76889
	+ http://battlelog.battlefield.com/bf4/servers/getNumPlayersOnServer/pc/c5ecddf9-0d34-4a70-8652-f7ed1c9e29ae/ (UUID)

