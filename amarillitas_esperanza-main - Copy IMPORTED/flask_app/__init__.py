from flask import Flask

app = Flask(__name__)

app.secret_key = "amarillitas"


app.config['UPLOAD_FOLDER'] = 'flask_app/static/img'