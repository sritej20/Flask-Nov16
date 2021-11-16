from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Welcome to my site</h1>"

@app.route("/hello")
def hello():
    return "<h1>Hello World</h1>"

@app.route("/hello/aus")
def aussie():
    return "<h1>G'Day Mate</h1>"

@app.route("/goodbye")
def goodbye():
    return "<h1>Seeya</h1>"