import pandas as pd
import sys

path = sys.argv[1]

xl = pd.ExcelFile(path)
dfs = pd.read_excel(path)

print(xl.sheet_names)

for column in range(dfs.shape[1]):
    for row in range(dfs.shape[0]):
        cell = dfs.iat[row, column]

        if pd.notnull(dfs.iat[row, column]):
            print(dfs.iat[row, column])

#print(dfs.shape[0])
#print(dfs.shape[1])

#print(dfs.loc[3])
