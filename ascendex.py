import requests
import time
import asyncio
import aiohttp

class Ascendex:
    def __init__(self):
        self.headers = {"Content-Type": "application/json"}
        self.urlOrderbooks = f"https://ascendex.com/api/pro/v1/depth?symbol="
        self.urlMarkets = f"https://ascendex.com/api/pro/v1/margin/products"
        self.fees = {'SPOT': {'Maker': {'LMCA': 0.1, 'Altkoins': 0.2}, 'Taker': {'LMCA': 0.1, 'Altkoins': 0.2}},
                    'FUTURES': {'Maker': {'LMCA': 0.4, 'Altkoins': 0.4}, 'Taker': {'LMCA': 0.6, 'Altkoins': 0.6}}}
        self.markets = {}
        self.rateLimits = 126

    def get_markets(self):
        markets = requests.get(url=self.urlMarkets, headers=self.headers).json()
        for market in markets['data']:
            if 'USDT' in market['symbol']:
                coin = market['symbol'].split('/USDT')[0]
                self.markets.update({coin: market['symbol']})
        return self.markets

    def get_all_fees(self):
        return {'comission': self.fees}

    async def get_orderbook(self, symbol):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.urlOrderbooks + symbol) as response:
                ob = await response.json()
        return {'top_ask': ob["data"]["data"]["asks"][0][0], 'ask_vol': ob["data"]["data"]["asks"][0][1],
                'top_bid': ob["data"]["data"]["bids"][0][0], 'bid_vol': ob["data"]["data"]["bids"][0][1],
                'ts_exchange': ob["data"]["data"]["ts"]}
        # return ob

async def main():
    orderbook = Ascendex()
    # result = await orderbook.get_orderbook('BTC/USDT')
    # print(result)
    while True:
        t0 = time.time()
        result = asyncio.create_task(orderbook.get_orderbook('BTC/USDT'))
        await result
        print(time.time() - t0)

if __name__ == "__main__":
    markets = Ascendex()
    print(markets.get_markets())
    print(markets.get_all_fees())
    asyncio.run(main())