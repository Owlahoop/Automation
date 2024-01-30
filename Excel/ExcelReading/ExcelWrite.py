import openpyxl

wk = openpyxl.Workbook()
# Prints name of active sheet
print(wk.active.title)

sh = wk.active
sh.title = "NewSheetName"
print(sh.title)

# Inputs value into cell
sh['A4'].value = "New A4 Value"

# Creates new sheet in the project
wk.create_sheet(title="TestingW")

# Assign sheet to variable
sh1 = wk['TestingW']
sh1['A3'] = "111222233999"

# Remove sheet
wk.remove(wk['NewSheetName'])

# Saves project
wk.save("C:\\Users\\Ryan\\Desktop\\TestData.xlsx")
