import xlrd
import xlwt
from xlutils.copy import copy

loc = "/Users/georgyjose/Downloads/EI_ISQIP.xlsx"
workbook = xlrd.open_workbook(loc)
wb = copy(workbook)

sheet = workbook.sheet_by_index(0)
lis= []
for i in range(1,sheet.nrows):
    lis.append(str(sheet.cell_value(i,8)))
# print lis
for i,j in enumerate(lis):
    lis[i] = lis[i].split(',')

for i,j in enumerate(lis):
    lis[i] = lis[i][-1]

print (lis)
wb_copy = wb.get_sheet(0)
for i,j in enumerate(lis):
    wb_copy.write(i+1,18,j)
wb.save("EI_ISQIPS.xls")