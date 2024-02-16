#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: displays 'Hello HBNB!'
    /hbnb: displays 'HBNB'
    /c/<text>: display C followed by the value of the text variable
               (replace underscore _ symbols with a space )
    /python/<text>: display Python, followed by the value of the text
               variable (replace underscore _ symbols with a space ) 
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    return "C {}".format(text.replace("_", " "))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    return "Python {}".format(text.replace("_", " "))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
