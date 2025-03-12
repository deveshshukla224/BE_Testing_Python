from requests.auth import HTTPBasicAuth
import requests

#session is used to maintain the state of the request
#it has request capabilities along with additional information like cookies, headers, etc.

session = requests.Session()
session.auth = HTTPBasicAuth('user', 'password')

response = session.get("https://httpbin.org/basic-auth/user/password")
print(response.status_code)  # 200 if auth is successful
