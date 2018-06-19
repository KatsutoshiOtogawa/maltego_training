import requests
import json
url = "http://alice6.nem.ninja:7890/account/transfers/outgoing?address=NBZMQO7ZPBYNBDUR7F75MAKA2S3DHDCIFG775N3D"

response = requests.get(url)

json_data = json.loads(response.text)
print(json.dumps(json_data,indent=4))
'''
{
    "timeStamp": 101630152,
    "error": "Bad Request",
    "message": "address must be valid",
    "status": 400
}
'''