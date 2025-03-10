import requests
import json
import postAPIRequest
from utilities import readfromglobalproperties
from utilities.resources import APIResources


id_deepak = postAPIRequest.id_deepak
print("ID of Deepak in delete file",id_deepak)
#reading the api url from global properties by passing section and key
api_url = readfromglobalproperties.read_config_from_global_properties("API","URL")
print("API URL is ",api_url)
#creating the full url by appending the api url and the resource from a class in resources.py
full_url = f"{api_url}/{APIResources.users}/{id_deepak}"
response = requests.delete(full_url)
print(response.status_code)