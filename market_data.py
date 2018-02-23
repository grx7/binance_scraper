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

""" ** not working **
"""
#OLD TRADE LOOKUP(MARKET DATA)

symbol = 'BNTBTC'
#limit = '500'
endpoint = 'https://api.binance.com'
path = '/api/v1/historicalTrades?symbol='+symbol #+'&limit='+limit
url = endpoint+path

response = requests.get(url)
content = json.loads(response.text)
print content

"""
"""

"""
#COMPRESSED/AGGREGATE TRADES LIST

symbol = 'BNTBTC'
#limit = '500'
endpoint = 'https://api.binance.com'
path = '/api/v1/aggTrades?symbol='+symbol #+'&limit='+limit
url = endpoint+path

response = requests.get(url)
content = json.loads(response.text)
print content

"""

"""
#KLINE/CANDLESTICK DATA
symbol = 'BTCUSDT'
#limit = '500'
endpoint = 'https://api.binance.com'
path = '/api/v1/klines?symbol='+symbol+'&interval=15m' #+'&limit='+limit
url = endpoint+path

response = requests.get(url)
content = json.loads(response.text)


for num in range(0,499):
    print (content[num][4])

"""

"""
# 24HR TICKER PRICE CHANGE STATISTICS

symbol = 'BTCUSDT'
endpoint = 'https://api.binance.com'
path = '/api/v1/ticker/24hr?symbol='+symbol
url = endpoint+path

response = requests.get(url)
content = json.loads(response.text)
print content
"""
"""
# SYMBOL PRICE TICKER

symbol = 'NEOUSDT'
endpoint = 'https://api.binance.com'
path = '/api/v3/ticker/price?symbol='+symbol
url = endpoint+path

response = requests.get(url)
content = json.loads(response.text)
print content
"""
"""
# SYMBOL ORDER BOOK TICKER

symbol = 'BTCUSDT'
endpoint = 'https://api.binance.com'
path = '/api/v3/ticker/bookTicker?symbol='+symbol
url = endpoint+path

response = requests.get(url)
content = json.loads(response.text)
print content
"""
