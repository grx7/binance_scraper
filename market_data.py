import requests
import json

"""
response = requests.get("https://api.binance.com/api/v3/ticker/price")
content = json.loads(response.text)
print (content[0][u'price'])

"""


"""

#ORDER BOOK

symbol = 'BNTBTC'
limit = '10'
endpoint = 'https://api.binance.com'
path = '/api/v1/depth?symbol='+symbol+'&limit='+limit
url = endpoint+path

response = requests.get(url)
content = json.loads(response.text)
print content

"""

"""
#RECENT TRADE LIST

symbol = 'BNTBTC'
limit = '1000'
endpoint = 'https://api.binance.com'
path = '/api/v1/trades?symbol='+symbol+'&limit='+limit
url = endpoint+path

response = requests.get(url)
content = json.loads(response.text)
print content

"""

#OLD TRADE LOOKUP(MARKET DATA)

symbol = 'BNTBTC'
limit = '500'
endpoint = 'https://api.binance.com'
path = '/api/v1/historicalTrades?symbol='+symbol #+'&limit='+limit
url = endpoint+path

response = requests.get(url)
content = json.loads(response.text)
print content

