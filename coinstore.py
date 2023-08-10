import requests


class Coinstore:

    def __init__(self):
        self.headers = {"Content-Type": "application/json"}
        self.symbol = "BTCUSDT"
        self.urlOrderbooks = f"https://api.coinstore.com/api/v1/market/depth/{self.symbol}"

    def get_orderbook(self):
        orderbook = requests.get(url=self.urlOrderbooks, headers=self.headers).json()
        # print(orderbook)
        topAsk = float(orderbook["data"]["a"][0][0])
        topBid = float(orderbook["data"]["b"][0][0])
        return {"topAsk": topAsk, "topBid": topBid}

# coinstore = Coinstore()
# orderbook = coinstore.get_orderbook()
# print(orderbook)


