import requests, json
response = requests.get("http://127.0.0.1:5000/hello")
print(response.content.decode("utf-8") )

url = 'http://127.0.0.1:5000/hello'
headers = {'content-type': 'application/json'}
data = {"eventType": "AAS_PORTAL_START", "data": {"uid": "hfe3hf45huf33545", "aid": "1", "vid": "1"}}
params = {'sessionKey': '9ebbd0b25760557393a43064a92bae539d962103', 'format': 'xml', 'platformId': 1}
x = requests.post(url, params=params, data=json.dumps(data), headers=headers)

print(x.text)
