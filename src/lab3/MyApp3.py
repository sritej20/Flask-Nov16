from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Welcome to my site</h1>"

username ="none"
@app.route("/user",methods =['GET','POST'])
def hello():
    global username
    if request.method == 'POST':
       username = request.form['name']
       return "User name updated to " + username
    else:
        return "User name = " + username




