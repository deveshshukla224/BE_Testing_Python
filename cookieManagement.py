import requests

session = requests.Session()
data_cookie = {"name":"shivam"}
session.cookies.update(data_cookie)
response = session.get("https://httpbin.org/cookies/set")
#print(response.status_code)
#print(response.json()['cookies'])



# response2 = session.get("https://httpbin.org/cookies/set",params={"name":"komal"})
# print(response2.status_code)
# print(response2.json()['cookies'])

# response3 = session.get("https://httpbin.org/cookies")
# print(response3.status_code)
# print(response3.json()['cookies'])


response4 = requests.get("https://reqres.in/api/{resource}",params={"page":2,'per_page':1})
print(response4.status_code)
print(response4.json())
