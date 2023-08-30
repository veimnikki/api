import requests
import asyncio
import aiohttp

class Difx:
    def __init__(self):
        self.headers = {"Content-Type": "application/json"}
        self.symbol = "BTCUSDT"
        self.urlOrderbooks = f"https://api-v2.difx.com/open/api/v1/orderbook?symbol="
        self.endOrderbooks = f"&level=2&depth=50"
        self.urlMarkets = f"https://api-v2.difx.com/open/api/v1/ticker"
        self.markets = {}

    def get_markets(self):
        markets = requests.get(url=self.urlMarkets, headers=self.headers).json()
        for market in markets:
            if '_USD' in market:
                coin = market.split('_USD')[0]
                self.markets.update({coin: market})
        return (self.markets)
        # return (markets)

    async def get_orderbook(self, symbol):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.urlOrderbooks + symbol + self.endOrderbooks) as response:
                ob = await response.json()
                # print(ob)
        return {"top_ask": ob["asks"][0][0], "top_bid": ob["bids"][0][0]}


difx = Difx()
markets = difx.get_markets()
print(markets)

async def main():
    orderbook = Difx()
    result = await orderbook.get_orderbook('BTC_USDT')
    print(result)

if __name__ == "__main__":
    asyncio.run(main())


# {'timestamp': 1692553971220, 'bids': [['26126.51', '0.332'], ['26124.7', '0.81713'], ['26123.26', '0.83009'], ['26122.47', '0.85118'], ['26122.18', '0.86656'], ['26118.76', '0.87988'], ['26116.81', '0.90285'], ['26116.38', '0.92072'], ['26115.94', '0.94618'], ['26114.98', '0.93041']], 'asks': [['26127.6', '0.01173'], ['26132.93', '0.01554'], ['26133.51', '0.04468'], ['26136.03', '0.01823'], ['26138.13', '0.01203'], ['26141.43', '0.71618'], ['26143.46', '0.7351'], ['26143.66', '0.74959'], ['26147.4', '0.76609'], ['26147.71', '0.77523']]}
