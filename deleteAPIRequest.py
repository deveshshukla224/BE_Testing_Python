import requests
import json
import postAPIRequest


id_deepak = postAPIRequest.id_deepak
print("ID of Deepak in delete file",id_deepak)
response = requests.delete('https://reqres.in/api/users/{id_deepak}')
print(response.status_code)