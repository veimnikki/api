import requests
import asyncio
import aiohttp

class Pointpay:
    def __init__(self):
        self.headers = {"Content-Type": "application/json"}
        self.urlOrderbooks = f"https://api.pointpay.io/api/v1/public/depth/result?market="
        self.endOrderbooks = f"&limit=25"
        self.urlMarkets = f"https://api.pointpay.io/api/v1/public/tickers"
        self.markets = {}

    def get_markets(self):
        markets = requests.get(url=self.urlMarkets, headers=self.headers).json()
        for market in markets['result']:
            if '_USD' in market:
                coin = market.split('_USD')[0]
                self.markets.update({coin: market})
        return(self.markets)
        # return(markets)

    async def get_orderbook(self, symbol):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.urlOrderbooks + symbol + self.endOrderbooks) as response:
                ob = await response.json()
                # print(ob)
        return {"top_ask": ob["asks"][0][0], "top_bid": ob["bids"][0][0]}


pointpay = Pointpay()
markets = pointpay.get_markets()
print(markets)

async def main():
    orderbook = Pointpay()
    result = await orderbook.get_orderbook('BTC_USDT')
    print(result)

if __name__ == "__main__":
    asyncio.run(main())