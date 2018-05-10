# coding=utf-8
from keys import *
from binance.client import Client

# import threading

# from binance.websockets import BinanceSocketManager

pair = "ZILBTC"

client = Client(api_key, api_secret)
bidLast = 0
askLast = 0

# for i in range(1000):
# 	depth = client.get_order_book(symbol=pair)
# 	bidNow = depth["bids"][0][0]
# 	askNow = depth["asks"][0][0]
# 	if bidLast < bidNow and askLast < askNow:
# 		print "1"
# 		print "BL: %s  BN: %s   AL: %s  AN: %s" % (bidLast, bidNow, askLast, askNow)
# 	else:
# 		print 0
# 	bidLast = bidNow
# 	askLast = askNow

	




candles = client.get_klines(symbol=pair, interval=Client.KLINE_INTERVAL_1MINUTE, limit=10)

print candles[0]


# def listsum(numList):
#     theSum = 0
#     for i in numList:
#         theSum = theSum + i
#     return theSum



# def CheckSumList(value, listCheck, listItems):
# 	if len(listCheck) == listItems:
# 		summListCheck = listsum(listCheck)
# 		listCheck = []
# 		print "Движение: %s" % (summListCheck)
# 	listCheck.append(value)
# 	return listCheck


# changeLine = []
# changeLine2 = []


# for i in range(1000):
# 	buyTrade = 0
# 	sellTrade = 0
# 	trades = client.get_recent_trades(symbol=pair, limit=30)
# 	lastTrade = trades[-1]
# 	lastPrice = str(lastTrade["price"])
# 	lastQ = str(lastTrade["qty"])
# 	for x in trades:
# 		if x["isBuyerMaker"]:
# 			sellTrade = sellTrade + float(x["qty"])
# 		else:
# 			buyTrade = buyTrade + float(x["qty"])


	
# 	stakan = buyTrade - sellTrade
# 	if len(changeLine) == 5:
# 		summlist = listsum(changeLine)
# 		if len(changeLine2) ==3:
# 			summlist2 = listsum(changeLine2)
# 			changeLine2 = []
# 			print "Движение: %s" %(summlist2)
# 		changeLine2.append(summlist)
# 		changeLine = []
# 	changeLine.append(stakan)



# 	# print stakan
	


