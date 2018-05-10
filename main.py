# coding=utf-8
from keys import *
from binance.client import Client

pair = "ZILBTC"





client = Client(api_key, api_secret)

# candles = client.get_klines(symbol=pair, interval=Client.KLINE_INTERVAL_5MINUTE)
# print candles

buyTrade = 0
sellTrade = 0

trades = client.get_recent_trades(symbol=pair, limit=30)
for x in trades:
	if x.["isBuyerMaker"]:
		buyTrade = buyTrade + x.["isBuyerMaker"]
	else
		sellTrade = sellTrade + x.["isBuyerMaker"]

print "buyTrade summ: %s" % (buyTrade) 
print " "
print "sellTrade summ: %s" % (sellTrade) 