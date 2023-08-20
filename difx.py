import requests


class Difx:
    def __init__(self):
        self.headers = {"Content-Type": "application/json"}
        self.symbol = "BTCUSDT"
        self.urlOrderbooks = f"https://api-v2.difx.com/open/api/v1/orderbook?symbol={self.symbol}&level=2&depth=50"

    def get_funcname(self):
        return Difx.__name__

    def get_orderbook(self):
        orderbook = requests.get(url=self.urlOrderbooks, headers=self.headers).json()
        # return orderbook
        topAsk = float(orderbook["asks"][0][0])
        ask_volume = float(orderbook["asks"][0][1])
        topBid = float(orderbook["bids"][0][0])
        bid_volume = float(orderbook["bids"][0][1])
        return {"topAsk": topAsk, "topBid": topBid, "ask_volume": ask_volume, "bid_volume": bid_volume}

# difx = Difx()
# orderbook = difx.get_orderbook()
# print(orderbook)

# {'timestamp': 1692553971220, 'bids': [['26126.51', '0.332'], ['26124.7', '0.81713'], ['26123.26', '0.83009'], ['26122.47', '0.85118'], ['26122.18', '0.86656'], ['26118.76', '0.87988'], ['26116.81', '0.90285'], ['26116.38', '0.92072'], ['26115.94', '0.94618'], ['26114.98', '0.93041']], 'asks': [['26127.6', '0.01173'], ['26132.93', '0.01554'], ['26133.51', '0.04468'], ['26136.03', '0.01823'], ['26138.13', '0.01203'], ['26141.43', '0.71618'], ['26143.46', '0.7351'], ['26143.66', '0.74959'], ['26147.4', '0.76609'], ['26147.71', '0.77523']]}
