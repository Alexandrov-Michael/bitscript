# coding=utf-8
from keys import *
from binance.client import Client

# import threading

# from binance.websockets import BinanceSocketManager

pair = "ZILBTC"
client = Client(api_key, api_secret)
# bidLast = 0
# askLast = 0

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

# import numpy as np
# import pandas as pd

# nda1 = np.array(candles)
# df = pd.DataFrame(nda1)

# def bollinger_strat(df, window, no_of_std):
#     rolling_mean = df[4].rolling(window).mean()
#     rolling_std = df[4].rolling(window).std()

#     df['Bollinger High'] = rolling_mean + (rolling_std * no_of_std)
#     df['Bollinger Low'] = rolling_mean - (rolling_std * no_of_std)    


# df['Bollinger High'] = rolling_mean + (rolling_std * 2)
# df['Bollinger Low'] = rolling_mean - (rolling_std * 2)    
# print bollinger_strat(df,5,2)

# changeLine = []

# def listsum(numList):
#     theSum = 0
#     for i in numList:
#         theSum = theSum + i
#     return theSum
stakanLast = 0

for i in range(1000):
	buyTrade = 0
	sellTrade = 0
	trades = client.get_recent_trades(symbol=pair, limit=30)
	lastTrade = trades[-1]
	lastPrice = str(lastTrade["price"])
	lastQ = str(lastTrade["qty"])
	for x in trades:
		if x["isBuyerMaker"]:
			sellTrade += float(x["qty"])
		else:
			buyTrade += float(x["qty"])
	stakan = buyTrade - sellTrade
	stakanChange = stakanLast - stakan
	print "Стакан: %s   Изменение стакана: %s" % (str(stakan), str(stakanChange))
	stakanLast = stakan



	# if len(changeLine) == 3:
	# 	summlist = listsum(changeLine)
	# 	changeLine = []
	# changeLine.append(stakan)
	


