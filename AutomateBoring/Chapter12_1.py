import openpyxl
# import os
#
# os.chdir("C:\\Users\\nuno.mota\\PycharmProjects\\AutomateBoring")
# print(os.getcwd())

wb = openpyxl.load_workbook('example.xlsx')

print(type(wb))

print(wb.get_sheet_names())

sheet = wb.get_sheet_by_name('Sheet3')

print(sheet.title)

print(type(sheet))

wb.active = 0
sheet = wb.get_sheet_by_name('Sheet1')

print(sheet.title)

print(tuple(sheet['A1':'C3']))

for rowOfCellObjects in sheet['A1':'C3']:
    for cellObj in rowOfCellObjects:
        print(cellObj.coordinate, cellObj.value)
    print('--- END OF ROW ---')
