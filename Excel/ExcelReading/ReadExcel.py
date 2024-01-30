# Import package
import openpyxl

# Load Workbook
wk = openpyxl.load_workbook("C:\\Users\\Ryan\\Desktop\\TestData.xlsx")

print(wk.sheetnames)
print("Active Sheet is " + wk.active.title)

# Create object of any sheet on which you want to work
sh = wk['Sheet1']
print(sh.title)
