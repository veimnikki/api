import requests


class Bigone:
    def __init__(self):
        self.headers = {"Content-Type": "application/json"}
        self.asset_pair_name = "BTC-USDT"
        self.urlOrderbooks = f"https://big.one/api/v3/asset_pairs/{self.asset_pair_name}/depth"

    def get_funcname(self):
        return Bigone.__name__

    def get_orderbook(self):
        orderbook = requests.get(url=self.urlOrderbooks, headers=self.headers).json()
        # return orderbook
        topAsk = float(orderbook["data"]["asks"][0]["price"])
        ask_volume = float(orderbook["data"]["asks"][0]["quantity"])
        topBid = float(orderbook["data"]["bids"][0]["price"])
        bid_volume = float(orderbook["data"]["bids"][0]["quantity"])
        return {"topAsk": topAsk, "topBid": topBid, "ask_volume": ask_volume, "bid_volume": bid_volume}

# bigone = Bigone()
# orderbook = bigone.get_orderbook()
# print(orderbook)

# {'code': 0, 'data': {'asset_pair_name': 'BTC-USDT', 'bids': [{'price': '26037.97', 'order_count': 1, 'quantity': '0.014291'}, {'price': '26037.84', 'order_count': 1, 'quantity': '0.021719'}, {'price': '26037.71', 'order_count': 1, 'quantity': '0.039891'}, {'price': '26037.58', 'order_count': 1, 'quantity': '0.031042'}, {'price': '26037.45', 'order_count': 1, 'quantity': '0.038768'}, {'price': '26023.22', 'order_count': 1, 'quantity': '0.54'}, {'price': '26023.21', 'order_count': 1, 'quantity': '0.02'}, {'price': '26020.8', 'order_count': 1, 'quantity': '0.03'}, {'price': '26018.72', 'order_count': 1, 'quantity': '0.05'}, {'price': '26012.27', 'order_count': 1, 'quantity': '0.34'}, {'price': '26012.26', 'order_count': 1, 'quantity': '0.38888'}, {'price': '25997.68', 'order_count': 1, 'quantity': '0.116435'}, {'price': '25995.08', 'order_count': 1, 'quantity': '0.143453'}, {'price': '25992.97', 'order_count': 1, 'quantity': '0.02'}, {'price': '25992.48', 'order_count': 1, 'quantity': '0.128643'}, {'price': '25989.87', 'order_count': 1, 'quantity': '0.134324'}, {'price': '25988.02', 'order_count': 1, 'quantity': '0.04'}, {'price': '25987.27', 'order_count': 1, 'quantity': '0.15756'}, {'price': '25962.61', 'order_count': 1, 'quantity': '0.00043'}, {'price': '25945.3', 'order_count': 1, 'quantity': '0.234'}, {'price': '25932.3', 'order_count': 1, 'quantity': '0.342'}, {'price': '25927.57', 'order_count': 1, 'quantity': '0.155105'}, {'price': '25919.3', 'order_count': 1, 'quantity': '0.576'}, {'price': '25914.56', 'order_count': 1, 'quantity': '0.130615'}, {'price': '25907.2', 'order_count': 1, 'quantity': '0.000595'}, {'price': '25901.54', 'order_count': 1, 'quantity': '0.113677'}, {'price': '25893.29', 'order_count': 1, 'quantity': '0.288'}, {'price': '25888.53', 'order_count': 1, 'quantity': '0.205045'}, {'price': '25847.45', 'order_count': 1, 'quantity': '0.000431'}, {'price': '25800', 'order_count': 1, 'quantity': '0.006058'}, {'price': '25797.56', 'order_count': 1, 'quantity': '0.43875'}, {'price': '25784.54', 'order_count': 1, 'quantity': '0.64125'}, {'price': '25777.6', 'order_count': 1, 'quantity': '0.000595'}, {'price': '25771.53', 'order_count': 1, 'quantity': '1.08'}, {'price': '25763.73', 'order_count': 1, 'quantity': '0.205549'}, {'price': '25758.52', 'order_count': 1, 'quantity': '0.675'}, {'price': '25753.32', 'order_count': 1, 'quantity': '0.216104'}, {'price': '25750', 'order_count': 1, 'quantity': '0.000979'}, {'price': '25745.51', 'order_count': 1, 'quantity': '0.54'}, {'price': '25742.91', 'order_count': 1, 'quantity': '0.337714'}, {'price': '25732.79', 'order_count': 1, 'quantity': '0.000431'}, {'price': '25732.5', 'order_count': 1, 'quantity': '0.171486'}, {'price': '25722.09', 'order_count': 1, 'quantity': '0.118634'}, {'price': '25711.68', 'order_count': 1, 'quantity': '0.180498'}, {'price': '25701.27', 'order_count': 1, 'quantity': '0.258548'}, {'price': '25700', 'order_count': 1, 'quantity': '0.003417'}, {'price': '25690.86', 'order_count': 1, 'quantity': '0.154402'}, {'price': '25680.45', 'order_count': 1, 'quantity': '0.369843'}, {'price': '25670.04', 'order_count': 1, 'quantity': '0.206827'}, {'price': '25666.66', 'order_count': 1, 'quantity': '0.000961'}], 'asks': [{'price': '26042.37', 'order_count': 1, 'quantity': '0.018454'}, {'price': '26042.8', 'order_count': 1, 'quantity': '0.028299'}, {'price': '26043.56', 'order_count': 1, 'quantity': '0.029129'}, {'price': '26043.69', 'order_count': 1, 'quantity': '0.03888'}, {'price': '26043.82', 'order_count': 1, 'quantity': '0.044147'}, {'price': '26057.25', 'order_count': 1, 'quantity': '0.54'}, {'price': '26057.86', 'order_count': 1, 'quantity': '0.02'}, {'price': '26065.52', 'order_count': 1, 'quantity': '0.03'}, {'price': '26068.76', 'order_count': 1, 'quantity': '0.81'}, {'price': '26068.77', 'order_count': 1, 'quantity': '0.38888'}, {'price': '26068.78', 'order_count': 1, 'quantity': '0.05'}, {'price': '26075.81', 'order_count': 1, 'quantity': '0.127544'}, {'price': '26078.41', 'order_count': 1, 'quantity': '0.147754'}, {'price': '26081.01', 'order_count': 1, 'quantity': '0.157545'}, {'price': '26083.62', 'order_count': 1, 'quantity': '0.117654'}, {'price': '26086.22', 'order_count': 1, 'quantity': '0.135654'}, {'price': '26117.34', 'order_count': 1, 'quantity': '0.288'}, {'price': '26126.69', 'order_count': 1, 'quantity': '0.255105'}, {'price': '26130.37', 'order_count': 1, 'quantity': '0.234'}, {'price': '26135.61', 'order_count': 1, 'quantity': '0.02'}, {'price': '26139.7', 'order_count': 1, 'quantity': '0.230615'}, {'price': '26140', 'order_count': 1, 'quantity': '0.001267'}, {'price': '26143.4', 'order_count': 1, 'quantity': '0.342'}, {'price': '26146.61', 'order_count': 1, 'quantity': '0.04'}, {'price': '26152.71', 'order_count': 1, 'quantity': '0.211368'}, {'price': '26156.43', 'order_count': 1, 'quantity': '0.576'}, {'price': '26165.72', 'order_count': 1, 'quantity': '0.205045'}, {'price': '26166.4', 'order_count': 1, 'quantity': '0.000594'}, {'price': '26169.46', 'order_count': 1, 'quantity': '0.36'}, {'price': '26194.47', 'order_count': 1, 'quantity': '0.000429'}, {'price': '26200', 'order_count': 1, 'quantity': '0.007309'}, {'price': '26250', 'order_count': 1, 'quantity': '0.000977'}, {'price': '26258.19', 'order_count': 1, 'quantity': '0.54'}, {'price': '26271.21', 'order_count': 1, 'quantity': '0.43875'}, {'price': '26280', 'order_count': 1, 'quantity': '0.001267'}, {'price': '26284.22', 'order_count': 1, 'quantity': '0.64125'}, {'price': '26296', 'order_count': 1, 'quantity': '0.000594'}, {'price': '26297.24', 'order_count': 1, 'quantity': '1.08'}, {'price': '26310.25', 'order_count': 1, 'quantity': '0.675'}, {'price': '26311.18', 'order_count': 1, 'quantity': '0.002946'}, {'price': '26323.78', 'order_count': 1, 'quantity': '0.105549'}, {'price': '26334.21', 'order_count': 1, 'quantity': '0.216104'}, {'price': '26344.63', 'order_count': 1, 'quantity': '0.337714'}, {'price': '26355.06', 'order_count': 1, 'quantity': '0.471486'}, {'price': '26365.48', 'order_count': 1, 'quantity': '0.618634'}, {'price': '26375.91', 'order_count': 1, 'quantity': '1.780498'}, {'price': '26386.33', 'order_count': 1, 'quantity': '1.958548'}, {'price': '26396.76', 'order_count': 1, 'quantity': '1.154402'}, {'price': '26400', 'order_count': 1, 'quantity': '0.015345'}, {'price': '26407.18', 'order_count': 1, 'quantity': '1.369843'}]}}
