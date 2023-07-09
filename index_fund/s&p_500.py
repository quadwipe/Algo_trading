#importing libraries required
import numpy as np 
import pandas as pd 
import requests
import xlsxwriter
import math

#importing list of stocks
stocks=pd.read_csv('sp_500_stocks.csv')
#acquiring an API token
from hmm import IEX_CLOUD_API_TOKEN
#making API call
symbol = 'AAPL'
api_url=f'https://sandbox.iexapis.com/stable/stock/{symbol}/quote/?token={IEX_CLOUD_API_TOKEN}'
data=requests.get(api_url).json()
#parsing API call
price=data['latestPrice']
market_cap=data['marketCap']
#creating pandas dataframe
my_columns = ['Ticker', 'Price','Market Capitalization', 'Number Of Shares to Buy']
final_dataframe = pd.DataFrame(columns = my_columns)
final_dataframe = final_dataframe.append(
                                        pd.Series(['AAPL', 
                                                   data['latestPrice'], 
                                                   data['marketCap'], 
                                                   'N/A'], 
                                                  index = my_columns), 
                                        ignore_index = True)