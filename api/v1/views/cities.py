#!/usr/bin/python3

"""
create cities..
"""

from flask import jsonify, abort, request
from models.state import State
from models.city import City
from models import storage
from api.v1.views import app_views

@app_views.route('/states/<state_id>/cities', strict_slashes=False)

def get_cities_by_states(state_id):
    """
    Retrieves the list of all City objects of a state
    """
    state = storage.get(State, state_id)
    if not state:
        return abort(404)
    cities = [city.to_dict() for city in state.cities]
    return jsonify(cities)

@app_views.route('/cities/<city_id>', strict_slashes=False)
def get_city(city_id):
    """
    Retrieves the list of all City.
    """
    city = storage.get(City, city_id)
    if city:
        return jsonify(city.to_dict())
    else:
        return abort(404)

@app_views.route('cities/<city_id>', methods=['DELETE'], strict_slashes=False)
def delete_city(city_id):
    """
    Retrieves a City
    """
    city = storage.get(City, city_id)
    if city:
        storage.delete(city)
        storage.save()
        return jsonify({}), 200
    else:
        return abort(404)
