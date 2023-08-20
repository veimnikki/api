import sqlite3
# import comparision



conn = sqlite3.connect('api.db')  # creating a database with the name "api.db"
cursor = conn.cursor()  # creating cursor for executing SQL commands and fetch results

# creating new tables
create_table_query = '''
CREATE TABLE IF NOT EXISTS purchase (
    id INTEGER PRIMARY KEY,
    ask_exchange TEXT,
    bid_exchange TEXT,
    pair_buy REAL,
    pair_sell REAL,
    price_ask REAL,
    price_bid REAL,
    volume_ask_ REAL,
    volume_bid REAL,
    time TEXT
)
'''
cursor.execute(create_table_query)
conn.commit()

#insert our data
# insert_query = "INSERT INTO purchase (ask_exchange, bid_exchange, pair_buy, pair_sell, price_ask, price_bid, volume_ask, volume_bid, time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
# data_to_insert = [("Dex trade", "Whitebit", 0.42343, 31.432, 132.65, 121.7, 12.2, 2132.1, '09:45')]
# cursor.executemany(insert_query, data_to_insert)
# conn.commit()

# block with printing our data
select_query = "SELECT * FROM purchase"
cursor.execute(select_query)
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()
