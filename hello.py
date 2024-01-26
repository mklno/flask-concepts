from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>Hello, World!<h1>'

@app.route('/user/<name>')
def user(name):
	return '<h1>Hello, %s!<h1>' %name

@app.route('/user/<int:userId>')
def userId(userId):
	print(url_for('userId', userId=userId))
	return '<h1>Here is your user id %d.</h1>' %userId


if __name__ == '__main__':
	app.run()
	
