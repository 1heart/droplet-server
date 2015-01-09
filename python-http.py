import http.client, json

data = {
        'title': 'haha',
        'text': 'rofl'
}

headers = {'Content-type': 'application/json'}


h1 = http.client.HTTPConnection("sheltered-chamber-7333.herokuapp.com")
h1.request("POST", "data", json.dumps(data), headers)
response = h1.getresponse()
print(response.read().decode())