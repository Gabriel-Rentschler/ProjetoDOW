import pandas as pd
import sys
import readSheet

path = sys.argv[1]

xl = pd.ExcelFile(path)
df = pd.read_excel(path, sheet_name=0)

numSheets = len(xl.sheet_names)

for sheets in range(numSheets):

    res = input("Print sheet?")
    if res == "n":
        break
    if res == "y":
        df = pd.read_excel(path, sheet_name = sheets)
        print('')
        print('Nome da planilha: %s' %xl.sheet_names[sheets])

    for row in range(df.shape[0]):
        for column in range(df.shape[1]):
            cell = df.iat[row, column]

            if pd.notnull(df.iat[row, column]):
                readSheet.lePlanilha(cell, df, row, column)

        print('')
