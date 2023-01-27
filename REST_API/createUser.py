import requests

payload={
    "name": "Shilpa",
    "job": "Automation"
}
resp=requests.post("https://reqres.in/api/users", data=payload)
print(resp)
print(type(resp))
print(resp.json())
assert resp.json()['job'] == "Automation"