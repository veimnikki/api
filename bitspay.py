import requests
import asyncio
import time
import aiohttp

class Bitspay:
    def __init__(self):
        self.headers = {"Content-Type": "application/json"}
        self.urlOrderbooks = f"https://api.bitspay.io/orderbook/"
        self.urlMarkets = f"https://api.bitspay.io/getavailablepairs/"
        self.urlFees = f"https://api.bitspay.io/getSelectedMarket/"
        self.markets = {}
        self.fees = {}
        self.requestLimit = 1275

    def get_markets(self):
        markets = requests.get(url=self.urlMarkets, headers=self.headers).json()
        for market in markets['combinations']:
            if ('_USDT' in market) and ('USDC_USDT' not in market):
                coin = market.split('_USDT')[0]
                self.markets.update({coin: market})
        return (self.markets)
        # return(markets)

    def get_coin_fee(self, symbol):
        url = self.urlFees + symbol
        fees = requests.get(url=url, headers=self.headers).json()
        for fee in fees['marketdetails']:
            maker_fee = fee['buyfee']
            taker_fee = fee['sellfee']
            self.fees.update({symbol: {"Maker": maker_fee, "Taker": taker_fee}})
        return self.fees
        # return fees

    async def get_orderbook(self, symbol):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.urlOrderbooks + symbol) as response:
                ob = await response.json()
        return {"top_ask": ob["asks"][0]["price"], "ask_vol": ob["asks"][0]["quantity"],
                "top_bid": ob["bids"][0]["price"], "bid_vol": ob["bids"][0]["quantity"],
                "ts_exchange": 0}

async def main():
    orderbook = Bitspay()
    # result = await orderbook.get_orderbook('BTC_USDT')
    # print(result)
    while True:
        t0 = time.time()
        result = asyncio.create_task(orderbook.get_orderbook('BTC_USDT'))
        await result
        print(time.time() - t0)

if __name__ == "__main__":
    markets = Bitspay()
    print(markets.get_markets())
    print(markets.get_coin_fee('BTC_USDT'))
    asyncio.run(main())
