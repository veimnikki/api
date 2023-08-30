import requests
import aiohttp
import asyncio

class Woo:
    def __init__(self):
        self.headers = {"Content-Type": "application/json"}
        self.urlOrderbooks = f"https://api.woo.org/v1/public/orderbook/"
        self.urlMarkets = f"https://api.woo.org/v1/public/info"
        self.markets = {}

    def get_markets(self):
        markets = requests.get(url=self.urlMarkets, headers=self.headers).json()
        for market in markets['rows']:
            if '_USD' in market['symbol']:
                coin = market['symbol'].split('_USD')[0]
                self.markets.update({coin: market['symbol']})
        return (self.markets)
        # return(markets)

    async def get_orderbook(self, symbol):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.urlOrderbooks + symbol) as response:
                ob = await response.json()
                # print(ob)
        return {"top_ask": ob['asks'][0]['price'], "top_bid": ob['bids'][0]['price']}

woo = Woo()
markets = woo.get_markets()
print(markets)

async def main():
    orderbook = Woo()
    result = await orderbook.get_orderbook('SPOT_BTC_USDT')
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
