from binance.spot import Spot # including Spot library
import config

client = Spot() # my first spot object

print("client.time(): ",client.time())