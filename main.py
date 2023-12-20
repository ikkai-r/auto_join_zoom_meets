import openpyxl as op
import webbrowser as wb

#get the zoom meetings
dataframe = op.load_workbook("zoom_meets.xlsx")

df1 = dataframe.active

#read the cols and rows
for row in range(1, df1.max_row):
    for col in df1.iter_cols(1, df1.max_column):
        print(col[row].value)