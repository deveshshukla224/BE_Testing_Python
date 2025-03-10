import requests
import json
from payload import *

response = requests.post('https://reqres.in/api/users',data=addUserPayload())

print("Line 1",type(response))
print("Line 20",type(response.json()))
print(response.status_code)


id_deepak = response.json()['id']
print("ID of Deepak",id_deepak)

