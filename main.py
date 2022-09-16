from contextlib import nullcontext
from inspect import _void
from time import sleep
import pandas as pd
import requests
from percentage import percetageCalculator

# markets = requests.get('https://ftx.com/api/futures').json()
# df = pd.DataFrame(markets['result'])
# df.set_index('name', inplace = True)
# print(df.T['BTC-PERP'])

futures = requests.get('https://ftx.com/api/futures/BTC-PERP').json()
futuresLast = futures['result']['last']
differ = percetageCalculator(futuresLast,5)

while futuresLast > differ:
    futures = requests.get('https://ftx.com/api/futures/BTC-PERP').json()
    futuresLast = futures['result']['last']
    print(str(futuresLast) +' > '+ str(differ))
    sleep(10)
    
print('buy!')

# while futuresLast > futuresLast - futuresLast-futuresLast-%5

# print(futuresLast)
