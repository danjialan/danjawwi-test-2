import openpyxl,pprint

print('Opening workbook...')
wb = openpyxl.load_workbook('C:/Users/danjawwi/Desktop/python/excel/3.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')
countyData = {}
print('Reading rows...')
for row in range(2,sheet.max_row +1):
    state = sheet['B' + str(row)].value
    county = sheet['C'+ str(row)].value