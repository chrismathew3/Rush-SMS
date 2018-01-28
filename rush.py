#Creator: Chris Chacko Mathew
#Date: 01/25/18
#Purpose: Take a Spreadsheet of PNM's of Both Genders.  Find as many Boys as Possible.  Send them the desired Text Message

import xlrd 
import csv
plus = '+1'

#with open('boys.csv', 'rb') as f:
#	reader = csv.reader(f)
#	your_list = list(reader)

#if "Brandon" in your_list:
#	printf('found it')

#Open Spreadsheet File
workbook = xlrd.open_workbook('PNM.xlsx')

#Open Correct Sheet
if workbook.nsheets == 1:
	worksheet = workbook.sheet_by_index(0)
else:
	worksheet = workbook.sheet_by_name('Active-PNMs')

print('Sheet name is %s' %worksheet.name)

headers = worksheet.row(0)
from xlrd.sheet import ctype_text

for idx, cell_obj in enumerate(headers):
	cell_type_str = ctype_text.get(cell_obj.ctype, 'unknown type')
	#print('(%s) %s %s' %(idx, cell_type_str, cell_obj.value))
	#if "First Name (Legal)" in cell_obj.value:
	#	fni = idx
	if "Mobile No" in cell_obj.value:
		pni = idx
	if "Email" in cell_obj.value:
		emi = idx

#print('First Name (Legal) column is: %s' %(fni+1))
print('Mobile No column is: %s' %(pni+1))
print('Email column is: %s' %(emi+1))
email = worksheet.col_values(emi, 1)
phone = worksheet.col_values(pni, 1)
#first_name = worksheet.col_values(fni)
#from xlrd.sheet import ctype_text
#for idy, cell_obj in enumerate(phone):
#	for idx, cell_obj in range()

for row_index in range(1, worksheet.nrows):
	print worksheet.cell(row_index, pni).value
	


#ncols = worksheet.ncols
#for columns in worksheet.ncols:
#	print(worksheet.cell(columns,0).value)
