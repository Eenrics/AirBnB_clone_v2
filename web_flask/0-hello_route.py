#!/usr/bin/python3
'''
Starts the flask application
the flask runs on 0.0.0.0 on port 5000
the home page should return hello hbnb
'''
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route("/")
def index():
    '''
    the home page and return hello hbnb
    '''
    return "Hello HBNB!"

app.run(host="0.0.0.0")
