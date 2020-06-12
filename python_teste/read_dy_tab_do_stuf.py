import pandas as pd
from pathlib import Path
from tabulate import tabulate
import numpy as np

path = Path('c:/tmp/TesteOrdemVenda.xlsx')
pd.set_option('max_columns', None)
pd.options.display.width = None
df1 = pd.read_excel(path, shett_name='Folha1', skiprows=6)

print(df1.index)
print(df1.columns)

print(tabulate(df1))
print(df1.iat[3, 15])
dados = df1.iat[3, 6]
dados1 = df1.iat[3, 11]
updateaditivo = 
print(type(dados))
print(dados1)
