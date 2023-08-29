import requests
import time
import asyncio
import aiohttp

class Coinstore:
    def __init__(self):
        self.headers = {"Content-Type": "application/json"}
        self.symbol = "BTCUSDT"
        self.urlOrderbooks = f"https://api.coinstore.com/api/v1/market/depth/"
        self.urlMarket = f"https://api.coinstore.com/api/v1/ticker/price"
        self.markets = {}

    def get_markets(self):
        markets = requests.get(url=self.urlMarket, headers=self.headers).json()
        for market in markets['data']:
            if 'USD' in market['symbol']:
                coin = market['symbol'].split('USD')[0]
                self.markets.update({coin: market['symbol']})

        return(self.markets)

    def get_funcname(self):
        return Coinstore.__name__

    async def get_orderbook(self, symbol):
        async with aiohttp.ClientSession() as session:  # менеджер отправления запросов
            async with session.get(self.urlOrderbooks + symbol) as response:
                ob = await response.json()
                # print(ob)
        return {'top_ask': ob['data']['a'][0][0], 'top_bid': ob['data']['b'][0][0]}

async def main():
    orderbook = Coinstore()
    result = await orderbook.get_orderbook('BTCUSDT')
    print(result)

if __name__ == "__main__":
    asyncio.run(main())


# coinstore = Coinstore()
# orderbook = asyncio.run(coinstore.get_orderbook("BTCUSDT"))
# print(orderbook)
# markets = coinstore.get_markets()

# {'data': {'channel': '4@depth@5', 'a': [['26042.5', '1.091057', -1], ['26043.5', '0.003511', -1], ['26044', '0.001755', -1], ['26044.5', '0.001755', -1], ['26045', '0.001755', -1]], 'b': [['26034', '0.366629', 1], ['26033.5', '0.001104', 1], ['26033', '0.237299', 1], ['26032', '0.18101', 1], ['26031.5', '0.001104', 1]], 'level': 5, 'symbol': 'BTCUSDT', 'instrumentId': 4}, 'code': 0}
