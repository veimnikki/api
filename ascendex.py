import requests
#  import time
import asyncio
import aiohttp


class Ascendex:
    def __init__(self):
        self.headers = {"Content-Type": "application/json"}
        self.symbol = "BTC/USDT"
        self.urlOrderbooks = f"https://ascendex.com/api/pro/v1/depth?symbol="
        self.urlMarkets = f"https://ascendex.com/api/pro/v1/spot/ticker"
        self.markets = {}

    def get_markets(self):
        markets = requests.get(url=self.urlMarket, headers=self.headers).json()
        for market in markets['data']:
            if 'USD' in market['symbol']:
                coin = market['symbol'].split('USD')[0]
                self.markets.update({coin: market['symbol']})
        return (self.markets)

    async def get_orderbook(self, symbol):
        async with aiohttp.ClientSession() as session:  # менеджер отправления запросов
            async with session.get(self.urlOrderbooks + symbol) as response:
                ob = await response.json()
                # print(ob)
        return {'top_ask': ob["data"]["data"]["asks"][0][0], 'top_bid': ob["data"]["data"]["bids"][0][0]}

async def main():
    orderbook = Ascendex()
    result = await orderbook.get_orderbook('BTCUSDT')
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
