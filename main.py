from binance.spot import Spot  # including Spot library
# from pprint import pprint
import config
import time
# import readchar
from getkey import getkey

client = Spot(api_key=config.APY_KEY, api_secret=config.APY_SECRET_KEY)  # my first spot object
sell = False
priceNow = 0.0
sellPrice = 0.0
yn = 'y'
symbol1 = "BTCTUSD"
# price = float(client.ticker_price(symbol1).get('price'))
price = 26000
quantity = round(100/price, 5)
side = "BUY"

print("quantity: ", quantity)

params = {
    "symbol": symbol1,
    "side": side,
    "type": "LIMIT",
    "timeInForce": "GTC",
    "quantity": quantity,
    "price": price
}

response = client.new_order(**params)
print("response: ", response)
orderId1 = response.get('orderId')
getkey()
getOrderResponse = client.get_order(symbol=symbol1, orderId=orderId1)
print("getOrderResponse: ", getOrderResponse)

# pprint(client.klines("BTCTUSD","15m",limit=1))

# print("buy BTC at: ", price)
# buy = True
#
# while True and (yn != 'n'):
#     time.sleep(2.0)
#     priceNow = float(client.ticker_price(symbol1).get('price'))
#     print("priceNow: ", priceNow, " buyPrice: ", price)
#     if buy and (priceNow >= (price+1.0)):
#         price = priceNow
#         side = "SELL"
#         params = {
#             "symbol": symbol1,
#             "side": side,
#             "type": "LIMIT",
#             "timeInForce": "GTC",
#             "quantity": quantity,
#             "price": price
#         }
#         print(params)
#         response = client.new_order(**params)
#         # print(response)
#         print("sell BTC at: ", price)
#         sell = True
#         buy = False
#         print("buy again?: ")
#         yn = getkey()
#         # yn = readchar.readkey()
#
#     if sell and (yn != 'n'):
#         price = float(client.ticker_price(symbol1).get('price'))
#         side = "BUY"
#         quantity = round(100 / price, 5)
#         params = {
#             "symbol": symbol1,
#             "side": side,
#             "type": "LIMIT",
#             "timeInForce": "GTC",
#             "quantity": quantity,
#             "price": price
#         }
#         print(params)
#         response = client.new_order(**params)
#         # print(response)
#         print("buy BTC at: ", price)
#         sell = False
#         buy = True
#
# # pprint(client.ticker_price("BTCTUSD").get('price'))
