# import config
import requests
import sqlite3
from slackhandler import Slack

def getslackdata(token, database):


	# init sqlite cursor
	db = sqlite3.connect(database)
	cursor = db.cursor()

	# Purge existing DB data
	cursor.execute('DELETE FROM timezones')

	# init api handler
	api = Slack(token)
	response = api.get_users()

	if response.status :
		# store useful data to db

		# sanity = 5
		for user in response.data:
			try :
				if user['tz'] and user['tz_offset']:
					cursor.execute('INSERT INTO timezones VALUES(:tz,:tz_offset)', user)
			except Exception as  e:
				print "Ignored DB error of type ", type(e)
			# Limit data stored
			# sanity-=1
			# if sanity < 0:
			# 	break

	db.commit()
	db.close()

if __name__ == '__main__':
	pass
