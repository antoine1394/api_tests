import requests
parameters = {
    'name': 'testingAPI',
    'email': 'testing@i.ua',
    'number': '+380991234567'
}
response = requests.get('https://httpbin.org/get', params=parameters)
print(response.text)