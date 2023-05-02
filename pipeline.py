# imports
from forex_python.converter import CurrencyRates

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import glob
import os

# consolidated dataframes from folder

balance = glob.glob(os.path.join(r'C:\Users\vlaub\Dropbox\Pessoal\Victor\LTS Investments\database\database\balance', "*.csv"))
movement = glob.glob(os.path.join(r'C:\Users\vlaub\Dropbox\Pessoal\Victor\LTS Investments\database\database\movement', "*.csv"))

balance = pd.concat((pd.read_csv(f, parse_dates=['date'], dayfirst=True) for f in balance),
                     ignore_index=True
                     ).sort_values(by='date')#.set_index('date')

movement = pd.concat((pd.read_csv(f, parse_dates=['date'], dayfirst=True) for f in movement),
                      ignore_index=True
                      ).sort_values(by='date')#.set_index('date')

#currency converter

c = CurrencyRates()

balance.rename({'amount':'amount_raw'}, axis= 1, inplace= True)

balance['amount'] = balance.apply( lambda x: c.convert( x.currency, 'USD', x.amount_raw, x.date), axis = 1)
balance['exchange rate'] = balance['amount_raw'] / balance['amount']

movement.rename({'amount':'amount_raw'}, axis= 1, inplace= True)

movement['amount'] = movement.apply( lambda x: c.convert( x.currency, 'USD', x.amount_raw, x.date), axis = 1)
movement['exchange rate'] = movement['amount_raw'] / movement['amount']

# movement metrics

    # average stock price

last = movement.groupby(['name_1'])['price'].last().dropna()

avg_price = (movement
    .groupby(['name_1', 'currency'])
    .apply(
        lambda x: pd.Series([
            np.average(x['price'], weights=x['amount'])
        ], index=['Average Price'])
    )
    .reset_index()).dropna().sort_index().merge(last,on='name_1', how='outer')

# balance metrics

    # variation

balance_var = (balance.groupby('name_1')['amount'].last()/balance.groupby('name_1')['amount'].first())-1

    # balance final amount

balance_final = pd.DataFrame(balance.groupby('name_1')['amount'].last()).reset_index()

    # balance pivot table for calculating total value

balance_pivot = pd.DataFrame(balance.pivot(index= 'date', columns=['name_1'], values='amount').ffill()).reset_index()

# exports

#   main
balance.to_csv('balance.csv')
movement.to_csv('movement.csv')

#   balance
balance_var.to_csv('balance_var.csv')
balance_pivot.to_csv('balance_pivot.csv')
balance_final.to_csv('balance_final.csv')

#   movement
avg_price.to_csv('avg_price.csv')