import requests
import json

url = "https://api.imagga.com/v2/tags"

querystring = {"image_url":"https://images.unsplash.com/photo-1541963463532-d68292c34b19?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max"}

headers = {
    'accept': "application/json",
    'authorization': "Basic YWNjX2ZjZGFmZTI2MGI3NjdhMDowOWNhMzA4MWIxMTg0MzZhYWI3YWZmYzIxYTIyYzk4MQ=="
    }

response = requests.request("GET", url, headers=headers, params=querystring)
data = json.loads(response.text.encode("ascii"))

for i in range(6):
    tag = data["result"]["tags"][i]["tag"]["en"]
    print(tag)
