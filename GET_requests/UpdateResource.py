import json
import jsonpath
import requests

# API URL
url = 'https://reqres.in/api/users/2'
# read input Json File
file = open('/Users/macbook/Documents/DEMO TESTS/pythonProject5/create_a_user.json', 'r')
json_input = file.read()
request_json = json.loads(json_input)
# make PUT request in json input body
response = requests.put(url, request_json)
# validating response code
assert response.status_code == 200
#parse response content
response_json = json.loads(response.text)
updated_li = jsonpath.jsonpath(response_json, 'updatedAt')
print(updated_li[0])