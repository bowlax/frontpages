from frontpages import feed
from flask import Flask
app = Flask(__name__)

@app.route("/ping")
def ping():
    return "ping returned"

@app.route("/")
def feedXML():
    return feed().getFeedXML()