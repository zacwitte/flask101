from flask import Flask, redirect, render_template

app = Flask("my app")

@app.errorhandler(500)
def page_error(error):
    return (render_template('error.html'), 500)

@app.errorhandler(404)
def page_not_found(error):
    return redirect("/")

@app.route("/")
def index():
    return "Hello world!"

@app.route("/error")
def generate_error():
	raise Exception("dummy exception")
    
app.run()