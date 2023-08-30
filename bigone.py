import requests
import asyncio
import aiohttp

class Bigone:
    def __init__(self):
        self.headers = {"Content-Type": "application/json"}
        self.urlOrderbooks = f"https://big.one/api/v3/asset_pairs/"
        self.endOrderbook = "/depth"
        self.urlMarkets = f"https://big.one/api/v3/asset_pairs"
        self.markets = {}

    def get_markets(self):
        markets = requests.get(url=self.urlMarkets, headers=self.headers).json()
        for market in markets['data']:
            if '-USD' in market['name']:
                coin = market['name'].split('-USD')[0]
                self.markets.update({coin: market['name']})
        return(self.markets)

    async def get_orderbook(self, symbol):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.urlOrderbooks + symbol + self.endOrderbook) as response:
                ob = await response.json()
                # print(ob)
        return {"top_ask": ob["data"]["asks"][0]["price"], "top_bid": ob["data"]["bids"][0]["price"]}


bigone = Bigone()
markets = bigone.get_markets()
print(markets)

async def main():
    orderbook = Bigone()
    result = await orderbook.get_orderbook('BTC-USDT')
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
