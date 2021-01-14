from frontpages import feed
import flask
app = flask.Flask(__name__)

@app.route("/ping") # is it up
def ping():
    return "ping returned"

@app.route("/feed.xml") # for reading in an rss reader
def feedXML():
    response = flask.make_response(feed().getFeedXML())
    response.headers['Content-Type'] = "application/rss+xml"
    response.headers['charset'] = "utf-8"
    return response
    
@app.route("/") # for testing in a browser
def index():
    response = flask.make_response(feed().getFeedXML())
    response.headers['Content-Type'] = "application/xml"
    response.headers['charset'] = "utf-8"
    return response