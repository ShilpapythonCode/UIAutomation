import json

import requests

mydata=open("data.json", "r").read()
resp=requests.post("https://reqres.in/api/users", data=json.loads(mydata))
print(resp)
print(type(resp))
print(resp.json())
print(resp.json())
print(resp.headers.get("content-type"))
assert resp.json()['job'] == "Automation"
print("Hellow")   # This will show message
