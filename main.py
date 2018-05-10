# coding=utf-8
import * from keys

pair = "BNBBTC"




from binance.client import Client
client = Client(api_key, api_secret)

candles = client.get_klines(symbol=pair, interval=Client.KLINE_INTERVAL_5MINUTE)