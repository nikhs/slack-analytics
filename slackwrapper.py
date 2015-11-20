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

	SCOPES =			{"channels:write"	: ["channels.archive",
												"channels.create",
												"channels.invite",
												"channels.join",
												"channels.kick",
												"channels.leave",
												"channels.mark",
												"channels.rename",
												"channels.setPurpose",
												"channels.setTopic",
												"channels.unarchive"],
						"channels:history"	: ["channels.history"],
						"channels:read"		: ["channels.info","channels.list"],
						"chat:write"		: ["chat.delete","chat.update"],
						"chat:write:bot"	: ["chat.postMessage"],
						"chat:write:user"	: ["chat.postMessage"],
						"emoji:read"		: ["emoji.list"],
						"files:write:user"	: ["files.delete","files.upload"],
						"files:read"		: ["files.info","files.list"],
						"groups:write"		: ["groups.archive",
												"groups.close",
												"groups.create",
												"groups.createChild",
												"groups.invite",
												"groups.kick",
												"groups.leave",
												"groups.mark",
												"groups.open",
												"groups.rename",
												"groups.setPurpose",
												"groups.setTopic",
												"groups.unarchive"],
						"groups:history"	: ["groups.history"],
						"groups:read"		: ["groups.info","groups.list"],
						"im:write"			: ["im.close", "im.mark", "im.open"],
						"im:history"		: ["im.history"],
						"im:read"			: ["im.list"],
						"mpim:write"		: ["mpim.close", "mpim.mark", "mpim.open"],
						"mpim:history"		: ["mpim.history"],
						"mpim:read"			: ["mpim.list"],
						"pins:write"		: ["pins.add","pins.remove"],
						"pins:read"			: ["pins.list"],
						"reactions:write"	: ["reactions.add","reactions.remove"],
						"reactions:read"	: ["reactions.get","reactions.list"],
						"search:read"		: ["search.all","search.files","search.messages"],
						"stars:write"		: ["stars.add","stars.remove"],
						"stars:read"		: ["stars.list"],
						"team:read"			: ["team.info"],
						"users:read"		: ["users.getPresence","users.info","users.list"],
						"users:write"		: ["users.setActive","users.setPresence"]}

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

# Errors tih api authentication
class BadRequestError(ApiException):
	pass

# General errors with api calls (eg invalid endpoint, paramas etc)
class RequestDeniedError(ApiException):
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
		self.token = None


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
	
	def set_access_credentials(self, access_token):
		self.token = access_token

	def get_token(self):
		if not self.token:
			raise BadRequestError('No access token obtained')
		return self.token


class Slack(object):
	"""  Custom Slack API wrapper for basic info retrieval """

	def __init__(self):
		self.config = Config()
		self.oauth = Oauth("https://slack.com/oauth/authorize", self.config['oauth.access'])
		self.scope_methods = []


	""" Set basic auth info REQUORED
	params	:	client_id		-	Client ID of your APP
				client_secret	-	Client Secret of your APP
				redirect URI	-	Redirect uri can be a subset of the app's redirect uri
	"""
 	def set_oauth_info(self, client_id, client_secret, redirect_uri=None):
 		self.oauth.set_oauth_info(client_id, client_secret, redirect_uri)

 	def get_authorize_url(self, scope, state, team=None):
 		for s in scope.split():
 			if s not in self.config.SCOPES.keys():
				raise BadRequestError('scope not valid %s'%(s))
 			
		return self.oauth.get_authorize_url(scope, state, team=None)

 	def get_access_information(self,code):
		response = self.oauth.get_access_information(code) 		
		parsed_response = response.json()
		if not parsed_response['ok']:
			raise RequestDeniedError(parsed_response['error'])
		
		self.scope = parsed_response['scope'].split(',')
		for s in self.scope:
			try:
				self.scope_methods.append( self.config.SCOPES[s] )
			except KeyError:
				# Ignore and continue -- for now
				continue

		return parsed_response['access_token']

	def set_access_credentials(self, access_token):
		self.oauth.set_access_credentials(access_token)


	# General api list requests with extra args omitted -- for now

	def get_users_list(self, presence= None):
		return self._get_method('users.list', presence= presence)

	def get_team_info(self):
		return self._get_method('team.info')

	def get_stars_list(self):
		return self._get_method('stars.list')

	def get_files_list(self):
		return self._get_method('files.list')

	def get_channels_list(self):
		return self._get_method('channels.list')

	# For 'read' api methods ONLY -- for now
	def _get_method(self, api_method, **params):

		# method verification
		if api_method not in self.config.API_PATHS.keys():
			raise BadRequestError('Invalid method') 

		# scope verification -- omitted for now
		# if api_method not in self.scope_methods :
		# 	raise BadRequestError('Method outside available scope')

		# api method call
		params['token']= self.oauth.get_token()
		path = self.config[api_method]
		# print params
		response = requests.get(path,params)
		parsed_response = response.json()

		if not parsed_response['ok']:
			raise RequestDeniedError(parsed_response['error'])
		else:
			return parsed_response

