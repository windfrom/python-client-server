import requests, json
response = requests.get("http://127.0.0.1:5000/hello")
print(response.content.decode("utf-8") )

url = 'http://127.0.0.1:5000/hello'
x = requests.post(url)

print(x.text)
