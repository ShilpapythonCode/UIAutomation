import requests
# JsonViewer for Code to view in Json: 	http://jsonviewer.stack.hu/ --- Copy body from reqres.in

p={"page":2}
resp=requests.get("https://reqres.in/api/users", params=p)  #  ----With parameter
# resp=requests.get("https://reqres.in/api/users?page=2") ----Without parameter
json_responce=resp.json()
print(json_responce["total_pages"])
assert json_responce["total_pages"]==2, "Total number of pages not matching"
print(json_responce["total"])
assert json_responce["total"]==12, "Total is not matching"
print(json_responce["data"][0]['email'])
assert (json_responce["data"][0]['email']).endswith("reqres.in"),"Email format is not matching"
print(json_responce["data"][1]['first_name'])
assert json_responce["data"][1]['first_name']!=None , "Name is empty"