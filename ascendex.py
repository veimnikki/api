import requests


class Ascendex:
    def __init__(self):
        self.headers = {"Content-Type": "application/json"}
        self.symbol = "BTC/USDT"
        self.urlOrderbooks = f"https://ascendex.com/api/pro/v1/depth?symbol={self.symbol}"

    def get_funcname(self):
        return Ascendex.__name__

    def get_orderbook(self):
        orderbook = requests.get(url=self.urlOrderbooks, headers=self.headers).json()
        # return orderbook
        topAsk = float(orderbook["data"]["data"]["asks"][0][0])
        ask_volume = float(orderbook["data"]["data"]["asks"][0][1])
        topBid = float(orderbook["data"]["data"]["bids"][0][0])
        bid_volume = float(orderbook["data"]["data"]["bids"][0][1])
        return {"topAsk": topAsk, "topBid": topBid, "ask_volume": ask_volume, "bid_volume": bid_volume}

# ascendex = Ascendex()
# orderbook = ascendex.get_orderbook()
# print(orderbook)

# {'code': 0, 'data': {'m': 'depth-snapshot', 'symbol': 'BTC/USDT', 'data': {'ts': 1692550360098, 'seqnum': 34526335300, 'asks': [['26044.81', '0.0075'], ['26044.82', '0.152'], ['26046.88', '0.11634'], ['26052.85', '0.0098'], ['26056.2', '0.152'], ['26057.63', '0.22815'], ['26057.95', '0.21088'], ['26058.03', '0.19082'], ['26058.68', '0.23075'], ['26058.69', '0.0051'], ['26058.75', '0.00057'], ['26058.85', '0.00056'], ['26058.95', '0.00054'], ['26059.11', '0.2119'], ['26059.32', '0.00041'], ['26059.53', '0.00195'], ['26059.75', '0.2184'], ['26059.76', '0.21775'], ['26060', '0.00819'], ['26060.06', '0.11699'], ['26060.08', '0.008'], ['26060.1', '0.00566'], ['26060.31', '0.3003'], ['26060.32', '0.29965'], ['26068.2', '0.297'], ['26078.4', '0.297'], ['26088.85', '0.28503'], ['26110.1', '0.297'], ['26114.88', '0.28183'], ['26123', '0.759'], ['26127.89', '0.28588'], ['26148.73', '0.52772'], ['26156', '0.0253'], ['26175.9', '0.0099'], ['26178', '0.451'], ['26179.94', '0.27842'], ['26200', '0.0002'], ['26207.7', '0.297'], ['26226', '0.0253'], ['26246.28', '0.01'], ['26296', '0.0253'], ['26359.2', '0.297'], ['26366', '0.0253'], ['26405', '0.2'], ['26436', '0.0253'], ['26620.2', '0.021'], ['26922.67', '0.00073'], ['27000', '0.05'], ['27423.86', '0.00023'], ['27500', '0.05'], ['27780', '0.11'], ['28000', '0.05'], ['28025', '1'], ['28162', '1'], ['28253.56', '0.00023'], ['28300', '1'], ['28437', '1'], ['28500', '0.05'], ['28523.86', '0.00023'], ['28575', '1'], ['28600', '1'], ['28700', '1'], ['28800', '1'], ['28900', '1'], ['29000', '1.32047'], ['29100', '1'], ['29136', '0.01064'], ['29200', '1'], ['29230', '0.0002'], ['29240', '0.0002'], ['29250', '0.0002'], ['29300', '1.0002'], ['29350', '0.0002'], ['29400', '1.00312'], ['29500', '1.05332'], ['29550', '0.0002'], ['29600', '0.00224'], ['29680', '0.52662'], ['29690', '1'], ['29695', '0.00991'], ['29700', '1.0002'], ['29710', '1'], ['29720', '1'], ['29730', '1'], ['29740', '1'], ['29750', '0.0002'], ['29757', '0.96137'], ['29777', '1'], ['29797', '1'], ['29810', '0.00208'], ['29817', '1'], ['29836', '1'], ['29856', '1'], ['29876', '1'], ['29896', '1'], ['29915', '1'], ['29935', '1'], ['29955', '1'], ['29975', '1'], ['29999', '0.00532'], ['30000', '0.05'], ['30002.56', '0.00022'], ['30060.84', '0.003'], ['30085', '0.56817'], ['30090', '1'], ['30107', '1'], ['30110', '1'], ['30120', '1'], ['30130', '1'], ['30148', '1'], ['30150', '1'], ['30152', '1'], ['30156', '1'], ['30165', '1'], ['30170', '1'], ['30173', '1'], ['30181', '1'], ['30189', '1'], ['30190', '1'], ['30197', '1'], ['30205', '1'], ['30206', '1'], ['30210', '1'], ['30214', '1'], ['30222', '1'], ['30225.56', '0.00022'], ['30230', '1'], ['30239', '1'], ['30248', '1'], ['30258', '1'], ['30266', '1'], ['30297', '1'], ['30300', '0.00124'], ['30311', '1'], ['30329', '1'], ['30360', '1'], ['30364', '1'], ['30392', '1'], ['30400', '0.00019'], ['30417', '1'], ['30423', '1'], ['30455', '1'], ['30470', '1'], ['30480', '0.00125'], ['30486', '1'], ['30500', '0.08404'], ['30518', '1'], ['30523', '1'], ['30550', '1'], ['30576', '1'], ['30580', '1'], ['30615', '1'], ['30629', '1'], ['30650', '1'], ['30668', '1'], ['30682', '1'], ['30686', '1'], ['30704', '1'], ['30722', '1'], ['30735', '1'], ['30740', '1'], ['30750', '0.00323'], ['30758', '1'], ['30776', '1'], ['30788', '1'], ['30794', '1'], ['30812', '1'], ['30830', '1'], ['30841', '1'], ['30848', '1'], ['30850', '1'], ['30866', '1'], ['30884', '1'], ['30892', '1'], ['30894', '1'], ['30900', '1'], ['30934', '1'], ['30947', '1'], ['30950', '1'], ['30976', '1'], ['31000', '1.12038'], ['31018', '1'], ['31050', '1'], ['31060', '1'], ['31080', '1'], ['31090', '1'], ['31100', '1'], ['31130', '1'], ['31140', '1'], ['31150', '1'], ['31160', '1'], ['31180', '1'], ['31190', '1'], ['31220', '1'], ['31240', '1'], ['31250', '1'], ['31280', '1'], ['31310', '1'], ['31323.86', '0.00023'], ['31340', '1'], ['31370', '1'], ['31400', '1'], ['31430', '1'], ['31460', '1'], ['31490', '1'], ['31500', '0.05'], ['31520', '1'], ['31545.15', '0.00046'], ['31550', '1'], ['31554', '1'], ['31566', '1'], ['31578', '1'], ['31590', '1'], ['31602', '1'], ['31614', '1'], ['31626', '1'], ['31638', '1'], ['31650', '1'], ['31662', '1'], ['31674', '1'], ['31686', '1'], ['31698', '1'], ['31710', '1'], ['31722', '1'], ['31734', '1'], ['31746', '1'], ['31758', '1'], ['31770', '1'], ['31782', '1'], ['31794', '1'], ['31806', '1'], ['31818', '1'], ['31830', '1'], ['31842', '1'], ['31854', '1'], ['31866', '1'], ['31878', '1'], ['31890', '1'], ['31902', '1'], ['31914', '1'], ['31926', '1'], ['31938', '1'], ['31950', '1'], ['31962', '1'], ['31974', '1'], ['31986', '1'], ['31999.98', '0.00826'], ['32000', '1.05'], ['32020', '1'], ['32040', '1'], ['32047.23', '0.001'], ['32060', '1'], ['32080', '1'], ['32100', '1'], ['32120', '1'], ['32140', '1'], ['32160', '1'], ['32180', '1'], ['32200', '1'], ['32220', '1'], ['32240', '1'], ['32260', '1'], ['32280', '1'], ['32300', '1'], ['32320', '1'], ['32340', '1'], ['32360', '1'], ['32380', '1'], ['32400', '1'], ['32420', '1'], ['32440', '1'], ['32460', '1'], ['32480', '1'], ['32500', '1.0505'], ['32520', '1'], ['32540', '1'], ['32560', '1'], ['32580', '1'], ['32600', '1'], ['32620', '1'], ['32640', '1'], ['32660', '1'], ['32680', '1'], ['32700', '1'], ['32720', '1'], ['32740', '1'], ['32760', '1'], ['32780', '1'], ['32800', '1'], ['32820', '1'], ['32840', '1'], ['32860', '1'], ['32880', '1'], ['32900', '1'], ['32920', '1'], ['32940', '1'], ['32960', '1'], ['32980', '1'], ['33000', '1'], ['33171', '1'], ['33313', '1'], ['33455', '1'], ['33597', '1'], ['33739', '1'], ['33881', '1'], ['34023', '1'], ['34165', '1'], ['34235.89', '0.0002'], ['34307', '1'], ['34449', '1'], ['34591', '1'], ['34733', '1'], ['34875', '1'], ['35000', '0.00137'], ['35017', '1'], ['35159', '1'], ['35301', '1'], ['35443', '1'], ['35585', '1'], ['35727', '1'], ['35869', '1'], ['36011', '1'], ['36153', '1'], ['36295', '1'], ['36437', '1'], ['36579', '1'], ['36721', '1'], ['36863', '1'], ['37000', '1'], ['37523.56', '0.00022'], ['40000', '0.00018'], ['40645.53', '0.00826'], ['41999.02', '0.00613'], ['44338.31', '0.00297'], ['50000', '0.00053'], ['59000', '0.006']], 'bids': [['26024.81', '0.0077'], ['26024.8', '0.152'], ['26016.4', '0.152'], ['26016', '0.00239'], ['26004.05', '0.20345'], ['26003.99', '0.07262'], ['26003.97', '0.19552'], ['26003.96', '0.2756'], ['26003.95', '0.23425'], ['26003.56', '0.08892'], ['26003.14', '0.3081'], ['26003.03', '0.01119'], ['26003', '0.20085'], ['26002.95', '0.1072'], ['26002.73', '0.26325'], ['26002.71', '0.00671'], ['26002.58', '0.01093'], ['26001.99', '0.23141'], ['26001.98', '0.2626'], ['26001.97', '0.18552'], ['26001.5', '0.1165'], ['26001.18', '0.2398'], ['26001.17', '0.0526'], ['26000.1', '0.297'], ['25999.77', '0.00049'], ['25995.3', '0.297'], ['25981.9', '0.297'], ['25976.97', '0.57237'], ['25970.75', '0.1518'], ['25953.3', '0.48791'], ['25946', '0.0253'], ['25942.6', '0.759'], ['25940.29', '0.47713'], ['25936.64', '0.41873'], ['25936.63', '0.02218'], ['25935.75', '0.5'], ['25934.75', '0.3'], ['25916', '1'], ['25911.93', '0.55544'], ['25906.7', '0.451'], ['25883.89', '0.00038'], ['25883', '1'], ['25882.1', '0.297'], ['25876', '0.0253'], ['25875.4', '0.5358'], ['25850.01', '0.00836'], ['25850', '1'], ['25816', '1'], ['25806', '0.0253'], ['25783', '1'], ['25758.3', '0.297'], ['25750', '1'], ['25736', '0.0253'], ['25716', '1'], ['25701.01', '0.0013'], ['25683', '1'], ['25666', '0.0253'], ['25650', '1'], ['25625', '1'], ['25596', '0.0253'], ['25576.2', '0.152'], ['25500', '0.5203'], ['25420', '0.45181'], ['25400', '1.00078'], ['25352.33', '0.00394'], ['25310.6', '0.076'], ['25175', '1'], ['25100', '0.00796'], ['25000.01', '0.02'], ['25000', '0.557'], ['24950', '1'], ['24869', '0.00201'], ['24725', '1'], ['24500', '0.12428'], ['24100', '0.00145'], ['24000.01', '0.02'], ['24000', '0.05'], ['23780', '2.5'], ['23500', '0.00095'], ['23000', '0.40174'], ['22000', '0.0704'], ['21500', '0.00224'], ['21000', '0.00883'], ['20123', '0.019'], ['20000', '0.00092'], ['19000', '0.42577'], ['16000', '0.02293'], ['15000', '0.00333'], ['9990', '1.00465'], ['9790.59', '0.00719'], ['9485.52', '0.00444']]}}}
