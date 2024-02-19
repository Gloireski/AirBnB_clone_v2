#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /states_list: display a HTML page: (inside the tag BODY)
        H1 tag: States
        UL tag: with the list of all State objects present in DBStorage
                sorted by name (A->Z).
    /states/<id>: display a HTML page: (inside the tag BODY) 
    If a State object is found with this id: 
        H1 tag: "State:"
        H3 tag: "Cities:"
        UL tag: with the list of City objects linked to the State sorted
                by name (A->Z)
        LI tag: description of one City: <city.id>: <B><city.name></B>
    Otherwise:
        H1 tag: "Not found!"
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    all_states = storage.all(State)
    return render_template('7-states_list.html', states=all_states)


@app.route('/states/<id>', strict_slashes=False)
def state(id):
    """Displays an HTML page with info about <id>, if it exists."""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
