from flask import Flask, session, redirect, render_template, request

app = Flask(__name__)
app.secret_key = 'sef4f8j4f983j4f093j2f0293jr2093r'

@app.route('/')
def index():
	if 'username' in session:
		return 'Logged in as %s' % session['username']
	return 'You are not logged in'

@app.route('/login', methods=['POST'])
def login_post():
	session['username'] = request.form['username']
	return redirect("/")
	
@app.route('/login', methods=['GET'])
def login_get():
	return render_template('ex4.html')

@app.route('/logout')
def logout():
	session.pop('username', None)
	return redirect("/")

app.run(debug=True)