#!/usr/bin/python3
"""
Creates Flask app views
"""

from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status')
def app_status():
    """"
    """
    response = {'status': "OK"}
    return jsonify(response)
