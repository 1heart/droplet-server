import os
from flask import Flask, jsonify, request

app = Flask(__name__)

drops = []

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/post', methods=['POST'])
def post_data():
	drop = {}
	try:
		drop[title] = request.json['title']
		drop[user] = request.json['user']
		drop[text] = request.json['text']
		drop[lat] = request.json['lat']
		drop[longi] = request.json['longi']
		drop[score] = request.json['score']
	except:
		return "not all values were correct"
	drops.append(drop)
	return "ty 4 data"

@app.route('/get', methods=['GET'])
def get_data():
	return jsonify(drops)

# if __name__ == '__main__':
#     app.run()
