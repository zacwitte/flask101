from flask import Flask

app = Flask("my app")

@app.route("/")
def index():
    return "Hello world!"
    
app.run(debug=True)