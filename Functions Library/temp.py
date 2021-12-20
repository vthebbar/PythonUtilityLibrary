import ReadWriteExcel
path ="..//TestData/Data.xlsx"
row = ReadWriteExcel.get_row_count(path,"Sheet1")
print(row)

col = ReadWriteExcel.get_column_count(path,"Sheet1")
print(col)