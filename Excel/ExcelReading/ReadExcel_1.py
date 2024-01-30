# Import Package
import openpyxl

wk = openpyxl.load_workbook("C:\\Users\\Ryan\\Desktop\\TestData.xlsx")
sh = wk["Sheet1"]

# print (sh['A3'].value)
# print (sh['B4'].value)

c1 = sh.cell(column=1, row=3)
print(c1.value)

print(c1.row)
print(c1.column)
