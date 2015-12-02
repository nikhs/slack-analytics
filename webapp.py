from slackwrapper import Slack
import config
import random, string, os


if os.path.isfile("../config.py"):
	print "config.py not found"
	exit(1)


# Helper fn to generate random state string
def random_string(length=12):
	return ''.join(random.SystemRandom().choice(string.digits+string.ascii_lowercase) for _ in range(length))


class DataParser(object):
	""" handles json response data manipulation """
	def __init__(self, ):
		self.team_info = None
		self.channels = None
		self.users = None		
		self.files = None
		self.stars = None

	def parse_team_info(self, raw):
		self.team_info['name'] = raw['team']['name']
		self.team_info['link'] = "https://%s.slack.com/"%(str(raw['team']['domain']))
		self.team_info['img'] = raw['team']['icon']['image_34']

	def parse_users_list(self):
		pass

	def parse_files_list(self):
		pass

	def parse_stars_list(self):
		pass

	def parse_channels_list(self):
		pass

class Webapp(object):
	"""app controller"""
	def __init__(self, slack):
		self.slack = slack
		self.state = random_string()
		self.is_authenticated = False
		self.slack.set_oauth_info(**config.credentials)
		self.auth_url = slack.get_authorize_url( config.scopes, self.state)

		self.parser = DataParser()

	def get_auth_url(self):
		return self.auth_url

	def authenticate(self, request):
		code = request.args.get('code')
		if code is not None:
			# Validate state parameter
			recv_state = request.args.get('state')
			if recv_state == self.state:
				# If everythings in order obtain token
				token = self.slack.get_access_information(code)
				self.slack.set_access_credentials(token)
				self.is_authenticated = True

			return self.is_authenticated
			
		else:
			# If auth failed
			error = request.args.get('error')
			raise UserWarning

	def get_user_slack_data(self):
		""" Get relevant slack data"""
		self.parser.parse_team_info( self.slack.get_team_info() )
		
webapp = Webapp(Slack())