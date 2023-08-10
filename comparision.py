from dex_trade import DexTrade
from coinstore import Coinstore
from whitebit import Whitebit

# exchanges = [DexTrade(), Coinstore()]
client1 = DexTrade()
client2 = Coinstore()
client3 = Whitebit()

while True:

    orderbook1 = client1.get_orderbook()
    orderbook2 = client2.get_orderbook()
    orderbook3 = client3.get_orderbook()

    # if orderbook1['topAsk'] < orderbook2['topBid']:
    #     print("bingo")
    # elif orderbook2['topAsk'] < orderbook1['topBid']:
    #     print("bingo")

    if orderbook2['topAsk'] < orderbook3['topBid']:
        print("bingo")
    elif orderbook3['topAsk'] < orderbook2['topBid']:
        print("bingo")