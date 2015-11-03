import requests
from contextlib import contextmanager

@contextmanager
def request_error_handler():
	try:
		yield
	except requests.ConnectionError as e:
		print "No connection.Try again later..."
		exit(1)
	except requests.HTTPError as e:
		print "Invalid HTTP response recieved..."
	except requests.TooManyRedirects as e:
		print "Too many Redirects..."
	except requests.RequestException as e:	
		print type(e)
		exit(1)

# Response object to store and retrieve responses
class Response(object):
	def __init__(self):
		# boolean status
		self.status = False
		# data and error 
		self.data = None
		self.error = None

#Simple Slack API handler for only vital functions
class Slack(object):
	def __init__(self, token):
		self._base_url = "https://slack.com/api/"
		self._token = {'token':token}
		self._params = None
		self.response = Response()

	def get_users(self, presence = False):

		param = {}
		if presence:
			param.update({"presence":1}) 
		
		# Call user list endpoint
		self._get_request("users.list", *param)

		#Only return relevant data
		if self.response.status:
			self.response.data = self.response.data["members"]
		return self.response

	def _get_request(self, endpoint, **kwargs):
		
		# Base param needs token
		self._params = self._token

		# Construct param
		for key, value in kwargs:
			self._params[key] = value

		# Carry out request
		with request_error_handler():
			r = requests.get(self._base_url + endpoint, params = self._params)

		if r.status_code == requests.codes.ok:
			slack_response = r.json()
			slack_status =  slack_response["ok"]

			if slack_status :
				self.response.data = slack_response
				self.response.status = True

			# Handle error raised by Slack API
			else:
				self.response.error = slack_response
				self.response.status = False

		# Handle unsuccessful request responses
		else:
			self.response.status = False
			self.response.error = r.status_code

if __name__ == '__main__':
	pass