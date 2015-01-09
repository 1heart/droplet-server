import os
from flask import Flask, jsonify, request
import json

app = Flask(__name__)

drops = []

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/post', methods=['POST'])
def post_data():
	drop = {}
	try:
		drop["user"] = request.json['user']
	except:
		return "user value DNE"
	try:
		drop["text"] = request.json['text']
	except:
		return "text value DNE"
	try:
		drop["lat"] = request.json['lat']
	except:
		return "lat value DNE"
	try:
		drop["longi"] = request.json['longi']
	except:
		return "longi value DNE"
	try:
		drop["score"] = request.json['score']
	except:
		return "score value DNE"
	drops.append(drop)
	return "ty 4 data"

@app.route('/get', methods=['GET'])
def get_data():
	return json.dumps(drops)

# if __name__ == '__main__':
#     app.run()
