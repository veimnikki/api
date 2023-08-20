# HERE IS SOME ERROR WITH PATH
import requests


class Woo:
    def __init__(self):
        self.headers = {"Content-Type": "application/json"}
        self.symbol = "BTC/USDT"
        self.urlOrderbooks = f"https://api.woo.org/v1/public/orderbook/{self.symbol}"

    def get_funcname(self):
        return Woo.__name__

    def get_orderbook(self):
        orderbook = requests.get(url=self.urlOrderbooks, headers=self.headers).json()
        return orderbook
        # topAsk = float(orderbook["data"]["asks"][0]["price"])
        # ask_volume = float(orderbook["data"]["asks"][0]["quantity"])
        # topBid = float(orderbook["data"]["bids"][0]["price"])
        # bid_volume = float(orderbook["data"]["bids"][0]["quantity"])
        # return {"topAsk": topAsk, "topBid": topBid, "ask_volume": ask_volume, "bid_volume": bid_volume}

woo = Woo()
orderbook = woo.get_orderbook()
print(orderbook)
