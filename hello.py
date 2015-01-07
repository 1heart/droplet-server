import os
from flask import Flask, jsonify

app = Flask(__name__)

drops = {}

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/data', method=("POST",))
def post_data():
	if not request.json or not 'title' in request.json:
		abort(400)
	drops[request.json['location']] = request.json['string']
	
	return "ty 4 data"

@app.route('/data', method=("GET",))
def get_data():
	return jsonify(drops)