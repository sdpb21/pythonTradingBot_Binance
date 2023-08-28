from binance.spot import Spot  # including Spot library
# from pprint import pprint
import config
# import time
# import readchar
# from getkey import getkey, keys

client = Spot(api_key=config.APY_KEY, api_secret=config.APY_SECRET_KEY)  # my first spot object
buy = False
sell = False
priceNow = 0.0
buyPrice = 0.0
sellPrice = 0.0
yn = 'y'
price = 25850
quantity = round(100/price, 5)

print("quantity: ", quantity)

params = {
    "symbol": "BTCTUSD",
    "side": "BUY",
    "type": "LIMIT",
    "timeInForce": "GTC",
    "quantity": quantity,
    "price": price
}
# print(client.account_status())
response = client.new_order(**params)
print(response)

# print("client.time(): ",client.time())
#
# #pprint(client.klines("BTCTUSD","15m",limit=1))
#
# buyPrice = float(client.ticker_price("BTCTUSD").get('price'))
# print("buy BTC at: ",buyPrice)
# buy = True
#
# while True and (yn != 'n'):
#     time.sleep(2.0)
#     priceNow = float(client.ticker_price("BTCTUSD").get('price'))
#     print("priceNow: ",priceNow," buyPrice: ",buyPrice)
#     if buy and (priceNow > (buyPrice+1.0)):
#         sellPrice = priceNow
#         print("sell BTC at: ",sellPrice)
#         sell = True
#         buy = False
#         print("buy again?: ")
#         yn = getkey()
#         #yn = readchar.readkey()
#
#     if sell and (yn != 'n'):
#         buyPrice = float(client.ticker_price("BTCTUSD").get('price'))
#         print("buy BTC at: ",buyPrice)
#         sell = False
#         buy = True
#
# #pprint(client.ticker_price("BTCTUSD").get('price'))
