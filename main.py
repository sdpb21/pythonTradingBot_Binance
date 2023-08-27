from binance.spot import Spot # including Spot library
from pprint import pprint
import config

client = Spot() # my first spot object
buy = False
sell = False
price = 0.0

print("client.time(): ",client.time())

#pprint(client.klines("BTCTUSD","15m",limit=1))

price = float(client.ticker_price("BTCTUSD").get('price'))
print("buy BTC at: ",price)
buy = True

while True:
    pprint(float(client.ticker_price("BTCTUSD").get('price')))
#pprint(client.ticker_price("BTCTUSD").get('price'))
