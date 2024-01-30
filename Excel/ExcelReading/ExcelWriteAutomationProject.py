import openpyxl

wk = openpyxl.Workbook()

sh = wk.active
sh.title = "NewSheetName"

# Inputs value into cell
sh['A1'].value = "user1"
sh['A2'].value = 'user2'
sh['A3'].value = 'user3'
sh['A4'].value = 'user4'
sh['B1'].value = 'pass1'
sh['B2'].value = 'pass2'
sh['B3'].value = 'pass3'
sh['B4'].value = 'pass4'

# Saves project
wk.save("C:\\Users\\Ryan\\Desktop\\TData10.xlsx")