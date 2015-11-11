import random, string
import urllib
import requests

class Config(object):
	""" Config object for Slack """
	API_PATHS	=	{	"auth.test"				:	"auth.test",
						"oauth.access"			:	"oauth.access",
						# CHANNELS
						"channel.archive"		:	"channels.archive",
						"channel.create"		:	"channels.create",
						"channel.history"		:	"channels.history",
						"channel.info"			:	"channels.info",
						"channel.invite"		:	"channels.invite",
						"channel.join"			:	"channels.join",
						"channel.kick"			:	"channels.kick",
						"channel.leave"			:	"channels.leave",
						"channel.list"			:	"channels.list",
						"channel.mark"			:	"channels.mark",
						"channel.rename"		:	"channels.rename",
						"channel.setPurpose"	:	"channels.setPurpose",
						"channel.setTopic"		:	"channels.setTopic",
						"channel.unarchive"		:	"channels.unarchive",
						# CHAT
						"chat.delete"			:	"chat.delete",
						"chat.postMessage"		:	"chat.postMessage",
						"chat.update"			:	"chat.update",
						"emoji.list"			:	"emoji.list",
						# FILES
						"files.delete"			:	"files.delete",
						"files.info"			:	"files.info",
						"files.list"			:	"files.list",
						"files.upload"			:	"files.upload",
						# GROUPS
						"groups.archive"		:	"groups.archive",
						"groups.close"			:	"groups.close",
						"groups.create"			:	"groups.create",
						"groups.createChild"	:	"groups.createChild",
						"groups.history"		:	"groups.history",
						"groups.info"			:	"groups.info",
						"groups.invite"			:	"groups.invite",
						"groups.kick"			:	"groups.kick",
						"groups.leave"			:	"groups.leave",
						"groups.list"			:	"groups.list",
						"groups.mark"			:	"groups.mark",
						"groups.open"			:	"groups.open",
						"groups.rename"			:	"groups.rename",
						"groups.setPurpose"		:	"groups.setPurpose",
						"groups.setTopic"		:	"groups.setTopic",
						"groups.unarchive"		:	"groups.unarchive",
						# IM
						"im.close"				:	"im.close",
						"im.history"			:	"im.history",
						"im.list"				:	"im.list",
						"im.mark"				:	"im.mark",
						"im.open"				:	"im.open",
						# MPIM
						"mpim.close"			:	"mpim.close",
						"mpim.history"			:	"mpim.history",
						"mpim.list"				:	"mpim.list",
						"mpim.mark"				:	"mpim.mark",
						"mpim.open"				:	"mpim.open",
						# PINS
						"pins.add"				:	"pins.add",
						"pins.list"				:	"pins.list",
						"pins.remove"			:	"pins.remove",
						# REACTION
						"reactions.add"			:	"reactions.add",
						"reactions.get"			:	"reactions.get",
						"reactions.list"		:	"reactions.list",
						"reactions.remove"		:	"reactions.remove",
						"rtm.start"				:	"rtm.start",
						# SEARCH
						"search.all"			:	"search.all",
						"search.files"			:	"search.files",
						"search.messages"		:	"search.messages",
						"stars.add"				:	"stars.add",
						"stars.list"			:	"stars.list",
						"stars.remove"			:	"stars.remove",
						# TEAM
						"team.accessLogs"		:	"team.accessLogs",
						"team.info"				:	"team.info",
						"team.integrationLogs"	:	"team.integrationLogs",
						# USERS
						"users.getPresence"		:	"users.getPresence",
						"users.info"			:	"users.info",
						"users.list"			:	"users.list",
						"users.setActive"		:	"users.setActive",
						"users.setPresence"		:	"users.setPresence"}

	# BASE URL FOR ALL API CALLS
	API_BASE = "https://slack.com/api/"

	def __init__(self):
		pass;
		# SETUP ALL VALID API PATHS
		# for key in self.API_PATHS.keys():
			# self.API_PATHS[key] = self.API_BASE + self.API_PATHS[key] 

	def __getitem__(self,  key):

		if not isinstance(key, str) :
			raise TypeError

		if key in self.API_PATHS.keys():
			return self.API_BASE + self.API_PATHS[key] 
		else:
			raise KeyError


# Exceptions 
class ApiException(Exception):
	pass

class InvalidAuthException(ApiException):
	pass
class NotAuthenticatedError(InvalidAuthException):
	pass
class InvalidTokenError(InvalidAuthException):
	pass

class RequestDeniedException(ApiException):
	pass
class InvalidAccountError(RequestDeniedException):
	pass
class PermissionDeniedError(RequestDeniedException):
	pass
	


class Oauth(object):
	
	"""  Handle Oauth requests to Slack """


	def __init__(self, authorize_uri, oauth_access_uri):
		self.AUTHORIZE_URI = authorize_uri
		self.OAUTH_ACCESS_URI = oauth_access_uri

	""" Set basic auth info REQUORED
	params	:	client_id		-	Client ID of your APP
				client_secret	-	Client Secret of your APP
				redirect URI	-	Redirect uri can be a subset of the app's redirect uri
	"""
	def set_oauth_info(self, client_id, client_secret, redirect_uri=None):
		self._client_id = client_id
		self._client_secret = client_secret
		self._redirect_uri = redirect_uri


		""" Get url to redirect user to Slack Authorization Page 
		params : scope  -  REQUIRED. Space seperated scopes( eg, 'files:read:bot search:read:user' )
				 state  -  State to prevent CSRF. Checked automatically
				 team   -  Restrict access to a Slack team
		return : string 
		"""
	def get_authorize_url(self, scope, state, team=None ):
		self.scope = scope
		self.state = state
		self._team = team

		self._oauth_url = {}

		self._oauth_url['client_id'] = self._client_id
		self._oauth_url['scope'] = self.scope
		self._oauth_url['state'] = self.state

		if self._redirect_uri:
			self._oauth_url['redirect_uri'] = self._redirect_uri
		if self._team:
			self._oauth_url['team'] = self.team

		return (self.AUTHORIZE_URI +'?'+ urllib.urlencode(self._oauth_url))



		""" Obtain access token from code
		params  :  code  - REQUIRED. code provided by slack on being authorized by user
		returns :  Response
		"""
	def get_access_information(self, code):
		self.code = code
		response = requests.get(self.OAUTH_ACCESS_URI, params={
			'client_id' : self._client_id,
			'client_secret' : self._client_secret,
			'code' : self.code,
			'redirect_uri' : self._redirect_uri
			})
		return response


class Slack(object):
"""  Custom Slack API wrapper """

	def __init__(self):
		self.config = Config()
		self.oauth = Oauth("https://slack.com/oauth/authorize", self.config['oauth.access'])


	""" Set basic auth info REQUORED
	params	:	client_id		-	Client ID of your APP
				client_secret	-	Client Secret of your APP
				redirect URI	-	Redirect uri can be a subset of the app's redirect uri
	"""
 	def set_oauth_info(self, client_id, client_secret, redirect_uri=None):
 		self.oauth.set_oauth_info(client_id, client_secret, redirect_uri)

 	def get_authorize_url(self, scope, state, team=None):
 		return self.oauth.get_authorize_url(scope, state, team=None)

 	def get_access_information(self,code):
		response = self.oauth.get_access_information(code) 		
		if not response.json['ok']:
			raise 

