from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/login', methods=['GET','POST'])
def login():
	if request.method == 'GET':
		return render_template('form.html')	
	if request.method == 'POST':
		print(request.form.to_dict())
		return '<p>%s</p>'  %request.headers
if __name__ == '__main__':
	app.run(debug=True)
