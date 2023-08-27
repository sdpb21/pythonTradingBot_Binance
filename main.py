from binance.spot import Spot # including Spot library
from pprint import pprint
import config

client = Spot() # my first spot object

print("client.time(): ",client.time())

#pprint(client.klines("BTCTUSD","15m",limit=1))

while True:
    pprint(float(client.ticker_price("BTCTUSD").get('price')))
#pprint(client.ticker_price("BTCTUSD").get('price'))
