import pandas as pd
import sys
import readSheet

path = sys.argv[1]

xl = pd.ExcelFile(path)
df1 = pd.read_excel(path, sheet_name=0)

numSheets = len(xl.sheet_names)

for sheets in range(numSheets):

    res = input("Print sheet?")
    if res == "n":
        break
    if res == "y":
        df1 = pd.read_excel(path, sheet_name = sheets)
        print('')
        print('Nome da planilha: %s' %xl.sheet_names[sheets])

    for row in range(df1.shape[0]):
        for column in range(df1.shape[1]):
            cell = df1.iat[row, column]

            if pd.notnull(df1.iat[row, column]):
                readSheet.lePlanilha(cell)

        print('')
