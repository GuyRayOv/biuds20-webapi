import requests

BASE = "https://jsonplaceholder.typicode.com"

# GET with query params
resp = requests.get(f"{BASE}/posts", params={"userId": 3})
resp.raise_for_status()
print (resp.json())         # list[dict]


# POST with JSON body
new_post = {"userId": 3, "title": "Hello", "body": "REST is simple"}
resp = requests.post(f"{BASE}/posts", json=new_post)
print(resp.status_code)     # 201
print(resp.json())

