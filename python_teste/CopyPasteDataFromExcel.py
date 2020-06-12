import glob
import os
import xlrd
import openpyxl
import tabulate as tb


list_of_files = glob.glob("C:\\Nkmix\\ForExcel\\*.xls")  # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getctime)

print(latest_file)

Orig_book = xlrd.open_workbook(filename=latest_file)

Orig_sheet = Orig_book.sheet_by_name('Matérias-Primas a utilizar')

Orig_data = [[Orig_sheet.cell_value(r, c) for c in range(Orig_sheet.ncols-2) if Orig_sheet.cell_value(r,c) !=""]  for r in range(Orig_sheet.nrows) if Orig_sheet.cell_value(r,0) != ""]
Orig_data.pop(0)

Dest_book = openpyxl.load_workbook(filename="Y:\\DadosActualizaçãoPowerBi\\Indicadores_Unidade_Alimentos_Compostos_2019.xlsx",data_only=True)

Dest_sheet = Dest_book.get_sheet_by_name('Folha1')

print(Dest_sheet['A1'].value)
Dest_sheet['A1'] = str(Orig_data[1])
print(Dest_sheet['A1'].value)
Dest_book.save("Y:\\DadosActualizaçãoPowerBi\\Indicadores_Unidade_Alimentos_Compostos_2019.xlsx")
print(Orig_data[1])
print(type(Orig_data))
print(len(Orig_data))
#print(tb.tabulate(Orig_data, tablefmt="plain"))
