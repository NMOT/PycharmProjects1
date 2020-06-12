import os
import pandas as pd
from pathlib import Path
from datetime import datetime

data_folder = Path('Y:/DadosActualizaçãoPowerBi/PrevisaoConsumos/')  # Search the most recent file in specified folder

latest_file = max(os.listdir(path=data_folder))

file_to_open = data_folder / latest_file

data = pd.read_excel(file_to_open, sheet_name="Matérias-Primas a utilizar", header=2,
                     usecols="A:C", na_filter=False, skiprows=1,
                     names=['CdNkmix', 'NomNkmix', 'QuantNkmix'], skipfooter=2)

ConsPrev = pd.DataFrame(data)  # Create Dataframe  with the data from excel file
date_time = datetime.fromtimestamp(os.path.getmtime(file_to_open))  # Add date of file to column in Dataframe

ConsPrev['Data Act'] = pd.to_datetime(date_time, yearfirst=True).date()
# ConsPrev = ConsPrev[ConsPrev.CdNkmix !='']

print(ConsPrev)
print(ConsPrev.head())
print(ConsPrev.info())
