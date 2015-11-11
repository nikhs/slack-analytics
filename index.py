from flask import Flask, url_for, render_template
import praw

app = Flask(__name__)

@app.route('/about')
def about():
	return "about"

@app.route('/')
def index():
	return render_template('index.html')


if __name__ == '__main__':
	app.run(debug=True)