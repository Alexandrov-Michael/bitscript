# coding=utf-8
from keys import *
from binance.client import Client

# import threading

# from binance.websockets import BinanceSocketManager

pair = "ZILBTC"

client = Client(api_key, api_secret)

# candles = client.get_klines(symbol=pair, interval=Client.KLINE_INTERVAL_5MINUTE)
# print candles




for i in range(1000):
	buyTrade = 0
	sellTrade = 0
	trades = client.get_recent_trades(symbol=pair, limit=30)
	lastPrice = str(trades[0]["price"])
	lastQ = str(trades[0]["qty"])
	for x in trades:
		if x["isBuyerMaker"]:
			sellTrade = sellTrade + float(x["qty"])
		else:
			buyTrade = buyTrade + float(x["qty"])


	# print "buyTrade summ: %s" % (buyTrade) 
	# print "sellTrade summ: %s" % (sellTrade) 
	# print " "
	msg = buyTrade - sellTrade
	# print "Разница: %s      buy: %s      sell: %s" % (msg, buyTrade, sellTrade)
	print "Разница: %s    Цена последняя: %s    Кол-во последнее: %s" %(msg, lastPrice, lastQ)
	# print lastPrice["price"]
	print " "



# def process_message(msg):
#     # print("message type: {}".format(msg['e']))
#     print(msg)
#     # do something



# bm = BinanceSocketManager(client)
# # start any sockets here, i.e a trade socket
# conn_key = bm.start_trade_socket(pair, process_message)
# # then start the socket manager
# bm.start()
		

