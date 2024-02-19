#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
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
    """
    Displays an HTML page with a list of all State objects in DBStorage.
    States are sorted by name.
    """
    all_states = storage.all(State)
    return render_template('7-states_list.html', states=all_states)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
