from flask import Flask, g
import MySQLdb

app = Flask(__name__)

@app.before_request
def before_request():
	g.db = MySQLdb.connect(passwd="foo",db="bar")
	
@app.route("/")
def index():
	c = g.db.cursor()
	c.execute("SELECT 1")
	
app.run(debug=True)