from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Welcome to my site</h1>"

@app.route("/user",methods =['GET','POST'])
def hello():
    if request.method == 'POST':
        return "Processed POST request"
    else:
        return "Processed GET request"




