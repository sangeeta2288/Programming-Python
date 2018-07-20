import xlrd
path="/Users/SanketSangeeta/Sangeeta_Applications/Python_DS/Socretica_Python/CSV/Google Stock Market Data - google_stock_data.csv")
file = xlrd.open(path)
for line in file:
	print(line)

