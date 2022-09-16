import pandas as pd
import requests
from percentage import percetageCalculator

# markets = requests.get('https://ftx.com/api/futures').json()
# df = pd.DataFrame(markets['result'])
# df.set_index('name', inplace = True)
# print(df.T['BTC-PERP'])
print(percetageCalculator(100,5))

futures = requests.get('https://ftx.com/api/futures/BTC-PERP').json()
futuresLast = futures['result']['last']
print(percetageCalculator(futuresLast,5))
# while futuresLast > futuresLast - futuresLast-futuresLast-%5

# print(futuresLast)
