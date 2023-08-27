from binance.spot import Spot # including Spot library
from pprint import pprint
import config
import time

client = Spot() # my first spot object
buy = False
sell = False
priceNow = 0.0
buyPrice = 0.0
sellPrice= 0.0

print("client.time(): ",client.time())

#pprint(client.klines("BTCTUSD","15m",limit=1))

buyPrice = float(client.ticker_price("BTCTUSD").get('price'))
print("buy BTC at: ",buyPrice)
buy = True

while True:
    time.sleep(2.0)
    priceNow = float(client.ticker_price("BTCTUSD").get('price'))
    #pprint(priceNow)
    if buy and (priceNow > buyPrice):
        sellPrice = priceNow
        print("sell BTC at: ",sellPrice)
        sell = True
        buy = False
        time.sleep(1.0)

    if sell:
        buyPrice = float(client.ticker_price("BTCTUSD").get('price'))
        print("buy BTC at: ",buyPrice)
        sell = False
        buy = True

#pprint(client.ticker_price("BTCTUSD").get('price'))
