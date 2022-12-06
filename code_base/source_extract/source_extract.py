import requests
import json
from data_generator import get_stock_data

symbol='MSFT'

response_API,time_zone=get_stock_data(symbol,outputsize='compact',freq='1min')
response_API[7]['time_zone']=time_zone

jsonStr = json.dumps(response_API)
print(jsonStr)

