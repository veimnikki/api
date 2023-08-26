from dex_trade import DexTrade
from coinstore import Coinstore
from whitebit import Whitebit
from bittrex import Bittrex
from bitspay import Bitspay
from ascendex import Ascendex
from bigone import Bigone
from difx import Difx
import datetime
import openpyxl

# workbook = openpyxl.workbook()
workbook = openpyxl.load_workbook('data_comparision.xlsx')
sheet = workbook.active

# sheet.append(['comparision number', 'ask purchase', 'bid purchase', 'pair/symbol', 'price (ask)', 'price (bid)',
#               'volume/amount (ask)', 'volume/amount (bid)', 'date', 'time'])

now = datetime.datetime.now()
symbol = 'BTCUSDT'
exchanges = {'DEXTRADE': DexTrade(), 'COINSTORE': Coinstore(), 'WHITEBIT': Whitebit(), 'BITTREX': Bittrex(),
             'BITSPAY': Bitspay(), 'ASCENDEX': Ascendex(), 'BIGONE': Bigone(), 'DIFX': Difx()}
opportunity_counter = 1
desired_iterations = len(exchanges)

i = 1
data_list = []

for exchange1, client1 in exchanges.items():
    done = {exchange1: []}
    for exchange2, client2 in exchanges.items():
        if not done.get(exchange2):
            done.update({exchange2: []})
        if exchange1 == exchange2 or exchange2 in done[exchange1] or exchange1 in done[exchange2]:
            continue

        done[exchange1].append(exchange2)
        orderbook1 = client1.get_orderbook()
        name_client1 = client1.get_funcname()
        orderbook2 = client2.get_orderbook()
        name_client2 = client2.get_funcname()

        if orderbook1['topAsk'] < orderbook2['topBid']:
            data = (
                i, name_client1, name_client2, symbol, orderbook1['topAsk'], orderbook2['topBid'],
                orderbook1['ask_volume'], orderbook2['bid_volume'], now.strftime("%d-%m-%Y"), now.strftime("%H:%M"))
            data_list.append(data)
            i += 1
        elif orderbook2['topAsk'] < orderbook1['topBid']:
            data = (
                i, name_client2, name_client1, symbol, orderbook2['topAsk'], orderbook1['topBid'],
                orderbook2['ask_volume'], orderbook1['bid_volume'], now.strftime("%d-%m-%Y"), now.strftime("%H:%M"))
            data_list.append(data)
            i += 1

for row in data_list:
    sheet.append(row)

workbook.save('data_comparision.xlsx')

opportunity_counter = 1
desired_iterations = len(exchanges)

# i = 0
# while opportunity_counter <= desired_iterations:
#     done = {}
#     for exchange1, client1 in exchanges.items():
#         done.update({exchange1: []})
#         for exchange2, client2 in exchanges.items():
#             if not done.get(exchange2):
#                 done.update({exchange2: []})
#             if exchange1 == exchange2:
#                 continue
#             elif exchange2 in done[exchange1] or exchange1 in done[exchange2]:
#                 continue
#
#             done[exchange1].append(exchange2)
#             orderbook1 = client1.get_orderbook()
#             name_client1 = client1.get_funcname()
#             orderbook2 = client2.get_orderbook()
#             name_client2 = client2.get_funcname()
#
#             # if orderbook1['topAsk'] < orderbook2['topBid']:
#             #     print("In",name_client1, "and", name_client2,"pair, the ask purchase is:", name_client1)
#             #     print("ask price:", orderbook1['topAsk'],", ask volume:", orderbook1['ask_volume'], "\nbid price:",
#             #           orderbook2['topBid'], ", bid volume:", orderbook2['bid_volume'], "\n")
#             # elif orderbook2['topAsk'] < orderbook1['topBid']:
#             #     print("In",name_client1, "and", name_client2,"pair, the ask purchase is:", name_client2)
#             #     print("ask price:", orderbook2['topAsk'], ", ask volume:", orderbook2['ask_volume'], "\nbid price:",
#             #           orderbook1['topBid'], ", bid volume:", orderbook1['bid_volume'], "\n")
#             # else:
#             #     print("In",name_client1, "and", name_client2,"pair no arbitrage opportunity:(", "\n")
#             # opportunity_counter += 1
#
#             if orderbook1['topAsk'] < orderbook2['topBid']:
#                 data = (
#                     ++i, name_client1, name_client2, symbol, orderbook1['topAsk'], orderbook2['topBid'], symbol,
#                      orderbook1['ask_volume'], orderbook2['bid_volume']), now.strftime("%d-%m-%Y"),
#                 now.strftime("%H:%M")
#             elif orderbook2['topAsk'] < orderbook1['topBid']:
#                 data = (
#                     ++i, name_client2, name_client1, symbol, orderbook2['topAsk'], orderbook1['topBid'], symbol,
#                      orderbook2['ask_volume'], orderbook1['bid_volume']), now.strftime("%d-%m-%Y"),
#                 now.strftime("%H:%M")
#             opportunity_counter += 1

# for row in data:
#     sheet.append(row)
#
# workbook.save('comparision2.xlsx')