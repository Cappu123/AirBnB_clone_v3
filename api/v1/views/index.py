#!/usr/bin/python3
"""
Creates Flask app views
"""

from api.v1.views import app_views
from flask import jsonify
from models import storage

@app_views.route('/status')
def app_status():
    """"
    """
    response = {'status': "OK"}
    return jsonify(response)
@app_views.route('/stats')
def get__tats():
    """
    """
    stats = {
        'amenities': storage.count('Amenity'),
        'cities': storage.count('City'),
        'places': storage.count('Place'),
        'reviews': storage.count('Review'),
        'states': storage.count('State'),
        'users': storage.count('User'),
        }
    return jsonify(stats)

