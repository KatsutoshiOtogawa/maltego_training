from  MaltegoTransform  import *

import requests
from datetime import datetime
import json

#nemの時間を取得する。
nemesisTime =  datetime(2015,3,29,9,6,25,0).timestamp()
#Nemのtimestampを通常のtimestampに変更する。
def nemTimestamp2timeStamp(nemTimeStamp):
    
    timeStamp = nemTimeStamp + int(nemesisTime)
    
    return datetime.fromtimestamp(timeStamp)

url = "http://alice6.nem.ninja:7890/account/transfers/outgoing?address="

#Maltego側で、パラメータの引数をNEMのアドレスに決め打ちしているので
#これでよい。
address_id = sys.argv[1]

res= requests.get(url + address_id)
domain = "hello"
if res.status_code == 200:
    json_data = json.loads(res.text)
    #このループごとにエンティティが追加される。
    for recipients in json_data['data']:
        try:
            me = MaltegoTransform()
            ent = me.addEntity("yourorganization.NEM",recipients['transaction']['recipient'])
            
            #entityのValueは文字列しか受け付けないので注意!!
            #エンティティのフィールドを動的に追加
            ent.addAdditionalFields(fieldName="Amount",displayName="Amount",matchingRule=True,value=str(recipients['transaction']['amount']))
            #いくら送金したかを表示
            ent.setLinkLabel(nemTimestamp2timeStamp(recipients['transaction']['timeStamp']).strftime('%Y/%m/%d %H:%M:%S'))

        except:
            pass

me.returnOutput()
