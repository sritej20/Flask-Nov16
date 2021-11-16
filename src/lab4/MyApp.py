from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def index():
    return "Welcome to the hello web service"


@app.route("/hello")
def hello():
   return "Hello anonymous user"

@app.route('/hello/<username>')
def helloname(username):
    if username == 'Jack' :
        return "HIT THE ROAD JACK!!!"
    else :
     return 'Hello {}'.format(username)

@app.route('/hello/<int:userid>')
def hellouserid(userid):	
    return 'Hello user unit number {:d}'.format(userid)

