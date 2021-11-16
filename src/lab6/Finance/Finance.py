from flask import Flask
# import requests
from urllib.request import urlopen 


app = Flask(__name__)

# The URL of the web service would not be hardcoded
# It would be supplied as part of the environment configureation


@app.route("/")
def index():
        #with urlopen("http://localhost:5000") as r:
        #        return r.read()
        return "Finance Department"

@app.route("/report")
def report() :
        return "No name supplied for credit report"

@app.route("/report/<client>")
def reportClient(client):
        with urlopen("http://localhost:5000/status/" + client) as r:
                status = bytes.decode(r.read()) 
                if status == "good":
                        return "Offer Financing" 
                if status == "bad" :
                        return "Decline Financing"
                return "More information needed"



