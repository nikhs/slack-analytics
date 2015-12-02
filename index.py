from flask import Flask, url_for, render_template, request, redirect, flash, session
from webapp import webapp
# from webapp import Webapp
# from slackwrapper import Slack
from config import app_secret

app = Flask(__name__)

@app.route('/about')
def about():
	return "about"

@app.route('/')
def index():
	return render_template('index.html', link=webapp.get_auth_url())

@app.route('/backhand/auth')
def authenticate():
	try:
		if webapp.authenticate(request):
			# flash("Logged in successfully")
			return redirect(url_for('.analytics'))
		else:
			flash("Login request invalid")
			return redirect(url_for('.analytics'))

	except UserWarning :
		flash("Slack Authentication failed")
		return redirect(url_for('.index'))

@app.route('/analytics')
def analytics():
	try:
		data = webapp.get_user_slack_data()
		return render_template('analytics.html', team= data.team, timezones=data.users, channels= data.channels)
	except Exception:
		return "It broke... :("

if __name__ == '__main__':
	app.config['SESSION_TYPE'] = 'filesystem'
	app.config['SECRET_KEY'] = app_secret

	app.debug = True
	app.run()