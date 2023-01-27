import requests

resp=requests.get("https://reqres.in/api/users?page=2")
code=resp.status_code
assert code==200 , "Status code doesn't match"

print(resp)
print(dir(resp))
print(type(resp))
print(resp.text)
print(resp.content)
print(resp.json())
print(resp.cookies)
print(resp.encoding)
print(resp.headers)
print(resp.url)
print(type(resp.headers))