import os
from flask import Flask, jsonify, request

app = Flask(__name__)

drops = {'lol': 'lol'}

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/data', methods=['POST'])
def post_data():
	request.
	return ""
@app.route('/get', methods=['GET'])
def get_data():
	return jsonify(drops)

# if __name__ == '__main__':
#     app.run()
