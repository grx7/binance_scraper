from binance.websockets import BinanceSocketManager
from binance.client import Client
bm = BinanceSocketManager(client)
# start any sockets here, i.e a trade socket
conn_key = bm.start_trade_socket('BNBBTC', process_message)
# then start the socket manager
#bm.start()
