import requests
url = "http://alice6.nem.ninja:7890/account/transfers/outgoing?address=NBZMQO7ZPBYNBDUR7F75MAKA2S3DHDCIFG775N3D"

response = requests.get(url)

print(response.text)

#帰って北結果
#{"timeStamp":101628624,"error":"Bad Request","message":"address must be valid","status":400}