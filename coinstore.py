import requests


class Coinstore:
    def __init__(self):
        self.headers = {"Content-Type": "application/json"}
        self.symbol = "BTCUSDT"
        self.urlOrderbooks = f"https://api.coinstore.com/api/v1/market/depth/{self.symbol}"

    def get_funcname(self):
        return Coinstore.__name__

    def get_orderbook(self):
        orderbook = requests.get(url=self.urlOrderbooks, headers=self.headers).json()
        # return(orderbook)
        topAsk = float(orderbook["data"]["a"][0][0])
        ask_volume = float(orderbook["data"]["a"][0][1])
        topBid = float(orderbook["data"]["b"][0][0])
        bid_volume = float(orderbook["data"]["b"][0][1])
        return {"topAsk": topAsk, "topBid": topBid, "ask_volume": ask_volume, "bid_volume": bid_volume}

# coinstore = Coinstore()
# orderbook = coinstore.get_orderbook()
# print(orderbook)

# {'data': {'channel': '4@depth@5', 'a': [['26042.5', '1.091057', -1], ['26043.5', '0.003511', -1], ['26044', '0.001755', -1], ['26044.5', '0.001755', -1], ['26045', '0.001755', -1]], 'b': [['26034', '0.366629', 1], ['26033.5', '0.001104', 1], ['26033', '0.237299', 1], ['26032', '0.18101', 1], ['26031.5', '0.001104', 1]], 'level': 5, 'symbol': 'BTCUSDT', 'instrumentId': 4}, 'code': 0}
