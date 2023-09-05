import requests
import asyncio
import aiohttp
import time


class Bittrex:
    def __init__(self):
        self.headers = {"Content-Type": "application/json"}
        self.marketSymbol = "BTC-USDT"
        self.depth = 25
        self.urlOrderbooks = f"https://api.bittrex.com/v3/markets/"
        self.endOrderbook = f"/orderbook?depth={self.depth}"
        self.urlMarkets = f"https://api.bittrex.com/v3/markets"
        self.markets = {}
        self.fees = {'SPOT': {'Maker': {'LMCA': 0.10, 'Altkoins': 0.10}, 'Taker': {'LMCA': 0.15, 'Altkoins': 0.15}},
                    'FUTURES': {'Maker': {'LMCA': 0.10, 'Altkoins': 0.10}, 'Taker': {'LMCA': 0.15, 'Altkoins': 0.15}}}
        self.requestLimit = 60

    def get_markets(self):
        markets = requests.get(url=self.urlMarkets, headers=self.headers).json()
        for market in markets:
            if ('-USDT' in market['symbol']) and ('USDC-USDT' not in market['symbol']):
                coin = market['symbol'].split('-USDT')[0]
                self.markets.update({coin: market['symbol']})
        return (self.markets)
        # return (markets)

    def get_all_fees(self):
        return self.fees

    async def get_orderbook(self, symbol):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.urlOrderbooks + symbol + self.endOrderbook) as response:
                ob = await response.json()
                # print(ob)
        return {"top_ask": ob["ask"][0]["rate"], "ask_vol": ob["ask"][0]["quantity"],
                "top_bid": ob["bid"][0]["rate"], "bid_vol": ob["bid"][0]["quantity"],
                "ts_exchange": 0}

async def main():
    orderbook = Bittrex()
    result = await orderbook.get_orderbook('BTC-USDT')
    print(result)
    # while True:
    #     t0 = time.time()
    #     result = asyncio.create_task(orderbook.get_orderbook('BTC_USDT'))
    #     await result
    #     print(time.time() - t0)

if __name__ == "__main__":
    markets = Bittrex()
    print(markets.get_markets())
    print(markets.get_all_fees())
    asyncio.run(main())

# {'bid': [{'quantity': '0.19021640', 'rate': '26086.207023090000'}, {'quantity': '0.03032362', 'rate': '26086.207023080000'}, {'quantity': '0.10448571', 'rate': '26074.717000000000'}, {'quantity': '0.01282686', 'rate': '26072.200000010000'}, {'quantity': '0.16605000', 'rate': '26072.200000000000'}, {'quantity': '0.42584400', 'rate': '26065.600000000000'}, {'quantity': '0.53157600', 'rate': '26047.780040010000'}, {'quantity': '0.00056044', 'rate': '26047.780040000000'}, {'quantity': '0.04000000', 'rate': '26039.900000000000'}, {'quantity': '0.10000000', 'rate': '26033.050000000000'}, {'quantity': '0.81486000', 'rate': '26033.000000000000'}, {'quantity': '1.05019200', 'rate': '26013.026100000000'}, {'quantity': '0.19221332', 'rate': '26012.765533060000'}, {'quantity': '0.53157600', 'rate': '26007.753150000000'}, {'quantity': '0.25000000', 'rate': '26000.928800000000'}, {'quantity': '0.26924400', 'rate': '26000.878800000000'}, {'quantity': '0.26924400', 'rate': '25995.248650000000'}, {'quantity': '0.26924400', 'rate': '25990.115800000000'}, {'quantity': '0.00015400', 'rate': '25985.735601220000'}, {'quantity': '0.26476200', 'rate': '25951.740900000000'}, {'quantity': '0.26476200', 'rate': '25948.605000000000'}, {'quantity': '0.00173461', 'rate': '25850.100000000000'}, {'quantity': '31.91152897', 'rate': '25850.000000000000'}, {'quantity': '0.25000000', 'rate': '25818.850000260000'}, {'quantity': '0.00100000', 'rate': '25735.734120000000'}], 'ask': [{'quantity': '0.00038360', 'rate': '26121.650490590000'}, {'quantity': '0.10000000', 'rate': '26121.650490600000'}, {'quantity': '0.06600000', 'rate': '26121.651490600000'}, {'quantity': '0.00105549', 'rate': '26133.160000000000'}, {'quantity': '0.16605000', 'rate': '26135.100000000000'}, {'quantity': '0.27915053', 'rate': '26137.799999990000'}, {'quantity': '0.42584400', 'rate': '26137.800000000000'}, {'quantity': '0.53157600', 'rate': '26138.689031990000'}, {'quantity': '0.01661538', 'rate': '26138.689032000000'}, {'quantity': '0.00095704', 'rate': '26152.179960000000'}, {'quantity': '0.25000000', 'rate': '26190.699000000000'}, {'quantity': '0.81486000', 'rate': '26190.700000000000'}, {'quantity': '1.05019200', 'rate': '26208.690900000000'}, {'quantity': '0.53157600', 'rate': '26221.756050000000'}, {'quantity': '0.26476200', 'rate': '26234.821200000000'}, {'quantity': '0.26476200', 'rate': '26241.353775000000'}, {'quantity': '0.26476200', 'rate': '26242.861500000000'}, {'quantity': '0.26476200', 'rate': '26252.306150000000'}, {'quantity': '0.26476200', 'rate': '26254.418925000000'}, {'quantity': '1.85638471', 'rate': '26488.762029080000'}, {'quantity': '0.00050000', 'rate': '26488.762029090000'}, {'quantity': '0.00107906', 'rate': '26500.000000000000'}, {'quantity': '0.00114267', 'rate': '26511.631400000000'}, {'quantity': '0.00016705', 'rate': '26550.400300230000'}, {'quantity': '0.00907793', 'rate': '26599.000000000000'}]}
