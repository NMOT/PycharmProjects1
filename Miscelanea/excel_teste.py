from openpyxl import Workbook

wb=Workbook()
ws=wb.active
ws.sheet_properties.tabColor = "1072BA"
#ws['A1']=490
wb.save("teste.xlsx")





