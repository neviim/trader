from binance.client import Client
from decouple import config

import matplotlib.pyplot as plt
import pandas as pd
import json
import os

api_key    = os.environ.get(config('BINANCEKEY'))
api_secret = os.environ.get(config('BINANCECHAVESECRETA'))

client = Client(api_key = api_key, api_secret = api_secret)

# todos os ultimos preços
ultimos_precos = client.get_all_tickers()
#print(precos)

# Livro de Ordens
asks_bids = client.get_order_book(symbol='BTCBRL')
#print(asks_bids)

# Preço medio
preco_medio = client.get_avg_price(symbol='BTCBRL')
#print(preco_medio)

# Pegando preços dointervalo de 1 dia
btcbrlDia = client.get_klines(symbol='BTCBRL', interval=Client.KLINE_INTERVAL_1DAY)
#print(btcbrlDia)

# tratando dados e arquiva em json
with open('../data/btc_df.json', 'w') as e:
    json.dump(btcbrlDia, e)

for line in btcbrlDia:
    del line[5:]

btc_df = pd.DataFrame(btcbrlDia, columns=['date', 'open', 'high', 'low', 'close'])
btc_df.set_index('date', inplace=True)
btc_df.index = pd.to_datetime(btc_df.index, unit='ms')
# print(btc_df.head())

btc_df['close'] = pd.to_numeric(btc_df['close'])
# btc_df['close'].plot()

# Media movel
mm_30 = btc_df.close.rolling(30).mean()
# mm_30.plot()

# Retornos, Histograma dos Retornos
ret_btc = btc_df['close'].pct_change()
# ret_btc.plot.hist(bins=60)

# Rolling-Vol - 30 days
vol_30 = ret_btc.rolling(30).std()
# vol_30.plot()

# Piores quedas dos últimos 30 dias
drawdown_30 = ret_btc.rolling(30).min()
# drawdown_30.plot()