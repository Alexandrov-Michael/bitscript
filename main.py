# coding=utf-8
from keys import *
from binance.client import Client

# import threading

# from binance.websockets import BinanceSocketManager

pair = "ZILBTC"

client = Client(api_key, api_secret)

# candles = client.get_klines(symbol=pair, interval=Client.KLINE_INTERVAL_5MINUTE)
# print candles


def listsum(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i
    return theSum

changeConst = 0
changeLine = []
dvigenie = ""


for i in range(1000):
	buyTrade = 0
	sellTrade = 0
	trades = client.get_recent_trades(symbol=pair, limit=30)
	lastTrade = trades[-1]
	lastPrice = str(lastTrade["price"])
	lastQ = str(lastTrade["qty"])
	for x in trades:
		if x["isBuyerMaker"]:
			sellTrade = sellTrade + float(x["qty"])
		else:
			buyTrade = buyTrade + float(x["qty"])


	
	stakan = buyTrade - sellTrade
	if len(changeLine) == 10:
		summlist = listsum(changeLine)
		changeLine = []
		print "Движение: %s" %(summlist)
	changeLine.append(stakan)
	# print stakan
	


