import pandas as pd
import yfinance as yf
df = pd.DataFrame()
tickerDf = yf.download("^GSPC SPY AAPL",period="ytd", group_by="ticker")
tickerDf.reset_index(level=0, inplace=True)
print(tickerDf)
#df.reset_index(level=0, inplace=True)
#print(df)

#data = yf.download(tickers="KO BCP.LS SPY AAPL")
#print(data)
"""
Isto é um teste do Github

"""

