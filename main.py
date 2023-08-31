from binance.spot import Spot  # including Spot library
# from pprint import pprint
import config
import time
# import readchar
from getkey import getkey
import pygame
from playsound import playsound

pygame.init()

client = Spot(api_key=config.APY_KEY, api_secret=config.APY_SECRET_KEY)  # my first spot object
sell = False
priceNow = 0.0
sellPrice = 0.0
yn = 'y'
symbol1 = "BTCTUSD"
price = float(client.ticker_price(symbol1).get('price'))
# price = 26000
usd = 200
quantity = round(usd/price, 5)
side = "BUY"

print("quantity: ", quantity)

# display = pygame.display.set_mode((300, 300))
# event = pygame.event.get()
# while not (event.type == pygame.KEYDOWN):
#     event = pygame.event.get()
#     playsound("/home/asdf/Downloads/beep-04.wav")
#     print(event)
#     time.sleep(2.0)

params = {
    "symbol": symbol1,
    "side": side,
    "type": "LIMIT",
    "timeInForce": "GTC",
    "quantity": quantity,
    "price": price
}

orderId1 = client.new_order(**params).get('orderId')
# print("orderId: ", orderId1)
# orderId1 = response.get('orderId')
status = client.get_order(symbol=symbol1, orderId=orderId1).get('status')
# print("status:", status)
# status = getOrderResponse.get('status')

# pprint(client.klines("BTCTUSD","15m",limit=1))

print("buy BTC at: ", price)
buy = True

while True and (yn != 'n'):
    time.sleep(2.0)
    while status != "FILLED":
        # time.sleep(1.0)
        print("waiting to get FILLED\n")
        status = client.get_order(symbol=symbol1, orderId=orderId1).get('status')
    priceNow = float(client.ticker_price(symbol1).get('price'))
    print("priceNow: ", priceNow, " buyPrice: ", price)
    if buy and (priceNow >= (price+3.0)):
        price = priceNow
        side = "SELL"
        params = {
            "symbol": symbol1,
            "side": side,
            "type": "LIMIT",
            "timeInForce": "GTC",
            "quantity": quantity,
            "price": price
        }
        print(params)
        response = client.new_order(**params)
        # print(response)
        print("sell BTC at: ", price)
        sell = True
        buy = False
        # creating display
        display = pygame.display.set_mode((300, 300))

        # creating a running loop
        alarm = True
        while alarm:

            # creating a loop to check events that
            # are occurring
            playsound("/home/asdf/Downloads/beep-04.wav")
            for event in pygame.event.get():
                # checking if keydown event happened or not
                if event.type == pygame.KEYDOWN:
                    print("A key has been pressed")
                    # if keydown event happened
                    # than printing a string to output
                    if event.key == pygame.K_ESCAPE:
                        print("Key ESC has been pressed")
                        alarm = False
            time.sleep(1.0)

        print("buy again?: ")
        yn = getkey()
        # yn = readchar.readkey()

    if sell and (yn != 'n'):
        price = float(client.ticker_price(symbol1).get('price'))
        side = "BUY"
        quantity = round(usd / price, 5)
        params = {
            "symbol": symbol1,
            "side": side,
            "type": "LIMIT",
            "timeInForce": "GTC",
            "quantity": quantity,
            "price": price
        }
        print(params)
        orderId1 = client.new_order(**params).get('orderId')
        status = client.get_order(symbol=symbol1, orderId=orderId1).get('status')
        while status != "FILLED":
            # time.sleep(1.0)
            print("waiting to get FILLED\n")
            status = client.get_order(symbol=symbol1, orderId=orderId1).get('status')
        print("buy BTC at: ", price)
        sell = False
        buy = True

pygame.quit()
