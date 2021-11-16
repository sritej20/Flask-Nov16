from flask import Flask
# from flask import request

app = Flask(__name__)

# Dummy credit status reporting
# Given a name, it returns whether or not that person has
# good or bad credit or has an unknown credit status

@app.route("/")
def index():
    return "Credit approval service."

@app.route("/status")
def status() :
    return "Please supply a name for credit status"

@app.route('/status/<username>')
def statusName(username):
    if username == 'Jack' :
        return "bad"
    if username == 'Walter':
        return "good"
    return "unknown"

