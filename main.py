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

# def CheckSumList(value, listCheck, listItems):
# 	if len(listCheck) == listItems:
# 		summListCheck = listsum(listCheck)
# 		listCheck = []
# 		print "Движение: %s" % (summListCheck)
# 	listCheck.append(value)
# 	return listCheck


changeLine = []
changeLine2 = []


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
	if len(changeLine) == 5:
		summlist = listsum(changeLine)
		if len(changeLine2) ==3:
			summlist2 = listsum(changeLine2)
			changeLine2 = []
			print "Движение: %s" %(summlist2)
		changeLine2.append(summlist)
		changeLine = []
	changeLine.append(stakan)



	# print stakan
	


