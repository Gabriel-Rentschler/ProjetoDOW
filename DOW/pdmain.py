import pandas as pd
import sys

path = sys.argv[1]

xl = pd.ExcelFile(path)
df1 = pd.read_excel(path, sheet_name=0)
df2 = pd.read_excel(path, sheet_name=1)

numSheets = len(xl.sheet_names)
print(xl.sheet_names)
print(numSheets)

for sheets in range(numSheets):

    res = input("Print sheet?")
    if res == "n":
        break
    if res == "y":
        df1 = pd.read_excel(path, sheet_name = sheets)
        print("Nome da planilha: " + df1.sheet_name)


    for row in range(df1.shape[0]):
        for column in range(df1.shape[1]):
            cell = df1.iat[row, column]

            if pd.notnull(df1.iat[row, column]):
                print(str(df1.iat[row, column]) + ' | ', end = '')

        print("")

#print(dfs.shape[0])
#print(dfs.shape[1])

#print(dfs.loc[3])
