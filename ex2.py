from flask import Flask, render_template
 
app = Flask(__name__)
 
@app.route("/<name>")
def index(name):
	return render_template('ex2.html',
		name=name, 
		sf_neighborhoods=[
		    'SOMA','Mission','Hayes Valley'])
    
if __name__ == "__main__":
	app.run(debug=True)