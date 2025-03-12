import requests
from utilities.resources import buildPayloadFromDBData

query = "SELECT * FROM users WHERE username = 'admin' AND password = 'password'"
requests.post("http://localhost:5000/dummy", json=buildPayloadFromDBData(query))