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
    /number/<n>: display n is a number only if n is an integer
    /number_template/<n>: display a HTML page only if n is an integer:
    H1 tag: Number: n inside the tag BODY
    /number_odd_or_even/<n>: display a HTML page only if n is an integer:
    H1 tag: Number: n is even|odd inside the tag BODY
    /states_list: display a HTML page: (inside the tag BODY)
        H1 tag: States
        UL tag: with the list of all State objects present in DBStorage
                sorted by name (A->Z).
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    all_states = storage.all(State)
    return render_template('7-states_list.html', states=all_states)


@app.teardown_appcontext
def teardown(exc):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
