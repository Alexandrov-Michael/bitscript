# coding=utf-8
from keys import *
from binance.client import Client

pair = "ZILBTC"





client = Client(api_key, api_secret)

# candles = client.get_klines(symbol=pair, interval=Client.KLINE_INTERVAL_5MINUTE)
# print candles




for i in range(10):
	buyTrade = 0
	sellTrade = 0
	trades = client.get_recent_trades(symbol=pair, limit=30)
	for x in trades:
		if x["isBuyerMaker"]:
			buyTrade = buyTrade + float(x["qty"])
		else:
			sellTrade = sellTrade + float(x["qty"])

	print "buyTrade summ: %s" % (buyTrade) 
	print "sellTrade summ: %s" % (sellTrade) 
	print " "