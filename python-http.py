import http.client, json

data = {
        'title': 'lol'
}

headers = {'Content-type': 'application/json'}


h1 = http.client.HTTPConnection('127.0.0.1:5000')
h1.request("POST", "data", json.dumps(data), headers)
response = h1.getresponse()
print(response.read().decode())