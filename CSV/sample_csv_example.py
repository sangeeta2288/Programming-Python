import xlrd
path="/Users/SanketSangeeta/Sangeeta_Applications/Python_DS/Socretica_Python/CSV/Google_Stock_Market_Data.xlsx"

file = xlrd.open(path)
for line in file:
	print(line)

