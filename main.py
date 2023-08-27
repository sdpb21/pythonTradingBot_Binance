from binance.spot import Spot # including Spot library
import config

client = Spot() # my first spot object

print("client.time(): ",client.time())

print(client.klines("BTCTUSD","15m",limit=1))

print(client.ticker_price("BTCTUSD"))