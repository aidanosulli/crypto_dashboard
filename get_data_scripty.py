from symtable import Symbol
import pandas as pd
import plotly.graph_objects as go
#Yahoo Finance Library
import yfinance as yf

#Alpha Vantage API 
from alpha_vantage.timeseries import TimeSeries
#Data viz
import plotly.graph_objs as go

# -----------------------------------------------------------------------------------------------------------------------


key = '7OWQW41NMRC1XQ2F' # My API Key
# https://github.com/RomelTorres/alpha_vantage
# Chose your output format or default to JSON (python dict)

ts = TimeSeries(key, output_format='pandas') # 'pandas' or 'json' or 'csv'
ttm_data, ttm_meta_data = ts.get_intraday(symbol='TTM',interval='1min', outputsize='compact')

print(ttm_meta_data)

df = ttm_data.iloc[:50].copy()
df=df.transpose()
df.rename(index={"1. open":"open", "2. high":"high", "3. low":"low",
                 "4. close":"close","5. volume":"volume"},inplace=True)
df=df.reset_index().rename(columns={'index': 'indicator'})
df = pd.melt(df,id_vars=['indicator'],var_name='date',value_name='rate')
df = df[df['indicator']!='volume']


df.to_csv("data/ttm.csv", index=False)

#Tried to use Alpha Vantage API for crypto data but it's not supported in the free version :(
#btc, btc_meta = ts.CRYPTO_INTRADAY(symbol = 'BTC', market = 'USD', interval = '1min', outputsize = 'compact')




#Let's use yahoo finance instead

#Bitcoin data
data = yf.download(tickers='BTC-USD', period = '24h', interval = '15m')

# data=data.transpose()
# data=data.reset_index().rename(columns={'index': 'indicator'})
# data = pd.melt(data,id_vars=['indicator'],var_name='date',value_name='price')
# data = data[data['indicator']!='volume']
data.to_csv("data/bitcoin.csv")

#Ethereum Data
data = yf.download(tickers='ETH-USD', period = '24h', interval = '15m')
# data=data.transpose()
# data=data.reset_index().rename(columns={'index': 'indicator'})
# data = pd.melt(data,id_vars=['indicator'],var_name='date',value_name='price')
# data = data[data['indicator']!='volume']
data.to_csv("data/ethereum.csv")

#USDT
data = yf.download(tickers='USDT-USD', period = '24h', interval = '15m')
# data=data.transpose()
# data=data.reset_index().rename(columns={'index': 'indicator'})
# data = pd.melt(data,id_vars=['indicator'],var_name='date',value_name='price')
# data = data[data['indicator']!='volume']
data.to_csv("data/tether.csv")



#Other Data Cleaning
line_data = pd.read_csv("data/world_crypto_usage.csv")

#String Replace stuff, convert to columns to ints
line_data['2019'] = line_data['2019'].str.replace("%", '')
line_data['2020'] = line_data['2020'].str.replace("%", '')
line_data['2021'] = line_data['2021'].str.replace("%", '')

line_data['2019'] = line_data['2019'].astype(int)
line_data['2020'] = line_data['2020'].astype(int)
line_data['2021'] = line_data['2021'].astype(int)

#Rename Column, Melt Data frame from 4 to 3 columns 
line_data.rename({"Characteristic":"Country"}, axis = 1, inplace= True)
line_data = pd.melt(line_data, 'Country', var_name= "Year", value_name = "Usage")
line_data.to_csv("data/world_crypto_usage2.csv")

exit()




# #declare figure
# fig = go.Figure()

# #Candlestick
# fig.add_trace(go.Candlestick(x=data.index,
#                 open=data['Open'],
#                 high=data['High'],
#                 low=data['Low'],
#                 close=data['Close'], name = 'market data'))

# # Add titles
# fig.update_layout(
#     title='Bitcoin live share price evolution',
#     yaxis_title='Bitcoin Price (kUS Dollars)')

# # X-Axes
# fig.update_xaxes(
#     rangeslider_visible=True,
#     rangeselector=dict(
#         buttons=list([
#             dict(count=15, label="15m", step="minute", stepmode="backward"),
#             dict(count=45, label="45m", step="minute", stepmode="backward"),
#             dict(count=1, label="HTD", step="hour", stepmode="todate"),
#             dict(count=6, label="6h", step="hour", stepmode="backward"),
#             dict(step="all")
#         ])
#     )
# )

# #Show
# fig.show()
