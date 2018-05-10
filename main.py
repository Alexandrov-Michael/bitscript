# coding=utf-8
from keys import *
from binance.client import Client

pair = "BNBBTC"





client = Client(api_key, api_secret)

candles = client.get_klines(symbol=pair, interval=Client.KLINE_INTERVAL_5MINUTE)
print candles