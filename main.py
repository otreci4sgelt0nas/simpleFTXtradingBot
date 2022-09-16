from time import sleep
import pandas as pd
import requests
from percentage import percetageCalculator
import FTXclass
import env_args

c = FTXclass.FtxClient(api_key=env_args.api_key, api_secret=env_args.api_secret)

# try:
#     check = c.get_open_orders(market='BTC-PERP')
#     print(check)
# except Exception as e:
#     print(f'Error checking for order status: {e}')

# markets = requests.get('https://ftx.com/api/futures').json()
# df = pd.DataFrame(markets['result'])
# df.set_index('name', inplace = True)
# print(df.T['BTC-PERP'])

# futures = requests.get('https://ftx.com/api/futures/BTC-PERP').json()
# futuresLast = futures['result']['last']
# differ = percetageCalculator(futuresLast,5)

# while futuresLast > differ:
#     futures = requests.get('https://ftx.com/api/futures/BTC-PERP').json()
#     futuresLast = futures['result']['last']
#     print(str(futuresLast) +' > '+ str(differ))
#     sleep(10)

#an example of buying
print('buy(ing)!')
try:
    r = c.place_order("BTC-PERP", "sell", 19.633, 0.0027, '1234','limit')
    print(r)
except Exception as e:
    print(f'Error making order request: {e}')
