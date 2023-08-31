import requests
import asyncio
import aiohttp

class Fairdesk:
    def __init__(self):
        self.headers = {"Content-Type": "application/json"}
        self.urlOrderbooks = f"https://api.fairdesk.com/api/v1/public/md/orderbook?symbol="
        self.urlMarkets = f"https://api.fairdesk.com/api/v1/public/products"
        self.markets = {}

    def get_markets(self):
        markets = requests.get(url=self.urlMarkets, headers=self.headers).json()
        for market in markets['data']:
            if '/USD' in market['displayName']:
                coin = market['displayName'].split('/USD')[0]
                self.markets.update({coin: market['displayName']})
        return(self.markets)
        # return(markets)

    async def get_orderbook(self, symbol):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.urlOrderbooks + symbol) as response:
                ob = await response.json()
                # print(ob)
        return {"top_ask": ob['data']["asks"][0][0], "top_bid": ob['data']["bids"][0][0]}


fairdesk = Fairdesk()
markets = fairdesk.get_markets()
print(markets)

async def main():
    orderbook = Fairdesk()
    result = await orderbook.get_orderbook('BTCUSDT')
    print(result)

if __name__ == "__main__":
    asyncio.run(main())