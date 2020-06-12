import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import style

import pandas_datareader.data as web


style.use('ggplot')

start = dt.datetime(2000, 1, 1)
end = dt.datetime(2016, 12, 31)

# df=web.DataReader('TSLA', 'yahoo', start, end)
#
# print(df.head())
#
# print(df.tail())

# df.to_csv('tsla.csv')

df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)

df['High'].plot()
plt.show()
#print(df.head())
