import requests
import json
from utilities import readfromglobalproperties
from utilities.resources import APIResources
from payload import *

api_url = readfromglobalproperties.read_config_from_global_properties("API","URL")
endpoint = APIResources.login
full_url = f"{api_url}{endpoint}"
print(full_url)
response = requests.post(full_url,auth=('eve.holt@reqres.in', 'cityslicka'))
print(response.status_code)
print(response.json())