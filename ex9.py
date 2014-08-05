from flask import Flask
from ex9_bp import simple_page

app = Flask(__name__)
app.register_blueprint(simple_page, url_prefix='/pages')

app.run(debug=True)