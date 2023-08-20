from dex_trade import DexTrade
from coinstore import Coinstore
from whitebit import Whitebit
from bittrex import Bittrex
from bitspay import Bitspay
from ascendex import Ascendex
from bigone import Bigone
from difx import Difx
import datetime

now = datetime.datetime.now()
exchanges = {'DEXTRADE': DexTrade(), 'COINSTORE': Coinstore(), 'WHITEBIT': Whitebit(), 'BITTREX': Bittrex(),
             'BITSPAY': Bitspay(), 'ASCENDEX': Ascendex(), 'BIGONE': Bigone(), 'DIFX': Difx()}
opportunity_counter = 1
desired_iterations = len(exchanges)

while opportunity_counter <= desired_iterations:
    done = {}
    for exchange1, client1 in exchanges.items():
        done.update({exchange1: []})
        for exchange2, client2 in exchanges.items():
            if not done.get(exchange2):
                done.update({exchange2: []})
            if exchange1 == exchange2:
                continue
            elif exchange2 in done[exchange1] or exchange1 in done[exchange2]:
                continue

            done[exchange1].append(exchange2)
            orderbook1 = client1.get_orderbook()
            name_client1 = client1.get_funcname()
            orderbook2 = client2.get_orderbook()
            name_client2 = client2.get_funcname()

            if orderbook1['topAsk'] < orderbook2['topBid']:
                print("In",name_client1, "and", name_client2,"pair, the ask purchase is:", name_client1)
                print("ask price:", orderbook1['topAsk'],", ask volume:", orderbook1['ask_volume'], "\nbid price:",
                      orderbook2['topBid'], ", bid volume:", orderbook2['bid_volume'], "\n")
            elif orderbook2['topAsk'] < orderbook1['topBid']:
                print("In",name_client1, "and", name_client2,"pair, the ask purchase is:", name_client2)
                print("ask price:", orderbook2['topAsk'], ", ask volume:", orderbook2['ask_volume'], "\nbid price:",
                      orderbook1['topBid'], ", bid volume:", orderbook1['bid_volume'], "\n")
            else:
                print("In",name_client1, "and", name_client2,"pair no arbitrage opportunity:(", "\n")
            opportunity_counter += 1

    print("time by Prague:", now.strftime("%d-%m-%Y %H:%M"))
    # if orderbook1['topAsk'] < orderbook2['topBid']:
    #     print("bingo")
    # elif orderbook2['topAsk'] < orderbook1['topBid']:
    #     print("bingo")

    # def addToDatabase(self):
    # return {"purchase exchange": orderbook1, "sale exchange": orderbook2}
# obj = Comparision("arg1_value", "arg2_value")