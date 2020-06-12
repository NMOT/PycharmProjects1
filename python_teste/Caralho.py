# 'dataset' contém os dados de entrada neste script
import glob
import os
import pandas as pd
from pathlib import Path

list_of_files = glob.glob("C:\\Nkmix\\ForExcel\\*.xls")

latest_file = max(list_of_files, key=os.path.getctime)

data = pd.read_excel(latest_file, sheet_name="Matérias-Primas a utilizar", header=2,
                     usecols=("A:C"), skip_footer=2, na_filter=True, skiprows=1,
                     names=['CodNkmix', 'NomNkmix', 'QuantPrev'])
print(latest_file)
ConsPrev = pd.DataFrame(data)

ConsPrev.insert(3, 'Data Act.', "")

date = latest_file[40:50]
print(date)
print(type(date))

ConsPrev['Data Act'] = pd.to_datetime(date, yearfirst=True)
print(ConsPrev)
