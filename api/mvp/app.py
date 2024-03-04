#!/usr/bin/python3
"This module defines endpoints for the food api"
from flask import Flask, make_response, jsonify
from api.mvp.views import app_apis


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_apis)

@app.errorhandler(404)
def not_found(error):
    """Handles 404 errors"""
    return make_response(jsonify({"error": "Not found"}), 404)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
