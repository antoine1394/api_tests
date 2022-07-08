import requests
import json
import jsonpath

# API URL
url = "https://reqres.in/api/users?page=2"
# send get request
response = requests.get(url)
# validate status code
print(response.status_code)
assert response.status_code == 200
# fetch response header
print(response.headers)
print(response.headers.get('Date'))
print(response.headers.get('Server'))
# fetch cookies
print(response.cookies)
# fetch encoding
print(response.encoding)
# fetch elapsed time
print(response.elapsed)
# parse response to Json format
json_response = json.loads(response.text)
print(json_response)
# fetch value using Json Path
page = jsonpath.jsonpath(json_response, 'page')
print(page)
total = jsonpath.jsonpath(json_response, 'total')
print(total)
# fetch specific value using advance Json Path
for i in range(0, 6):
    first_name = jsonpath.jsonpath(json_response, 'data['+str(i)+'].first_name')
    print(first_name)
# assertion of values
pages = jsonpath.jsonpath(json_response, 'total_pages')
assert pages[0] == 2
