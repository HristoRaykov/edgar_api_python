import os
import pandas as pd
import pandas_datareader as pdr

query = 'WIKI/AAPL'
data = pdr.DataReader('^DJI', 'stooq')


TIIANGO_API_KEY = os.getenv("TIIANGO_API_KEY")
# https://api.tiingo.com/tiingo/daily/ETY/prices?token=5bbb9e7c4c5aab5c84531c9b8bc04c3b56848e21
data = pdr.get_data_tiingo("XETYX", api_key=TIIANGO_API_KEY)
tickers = pd.read_csv("supported_tickers_tiingo.csv")
asset_types = tickers["assetType"].unique()
exchange = tickers["exchange"].unique()


data = pdr.get_data_yahoo("ETY", get_actions=True)  # adjust_price=True


data = pdr.data.DataReader("ETY", "iex")

