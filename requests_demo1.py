import requests
import json

response = requests.get('https://reqres.in/api/users',params={'page':2})
json_response = response.json()
print((json_response))