import requests
url = "http://www.yahoo.co.jp"

response = requests.get(url)

print(response.text)