import json
import jsonpath
import requests

# API URL
url = 'https://reqres.in/api/users'
# read input Json File
file = open('/Users/macbook/Documents/DEMO TESTS/pythonProject5/create_a_user.json', 'r')
json_input = file.read()
request_json = json.loads(json_input)
print(request_json)
# make POST request in json input body
response = requests.post(url, request_json)
assert response.status_code == 201
# fetch header from the response
print(response.headers.get('Content-Length'))
# parse response to json format
response_json = json.loads(response.text)
#pick id using json path
id = jsonpath.jsonpath(response_json, 'id')
print(id[0])