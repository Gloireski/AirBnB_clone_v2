#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /cities_by_states: display a html page (inside body)
        H1 tag: States
        UL tag: with the list of all State objects present in DBStorage
                sorted by name (A->Z)
        LI tag: description of one State: <state.id>: <B><state.name></B>
                + UL tag: with the list of City objects linked to the
                State sorted by name (A->Z) 
        LI tag: description of one City: <city.id>: <B><city.name></B>
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    all_states = storage.all(State)
    #all_cities = storage.all(City)
    return render_template('8-cities_by_states.html', states=all_states, cities=all_cities)


@app.teardown_appcontext
def teardown(exc):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
