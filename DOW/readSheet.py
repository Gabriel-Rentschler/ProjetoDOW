import pandas as pd

def lePlanilha(cell, df, row, column):

    if(row==0 or pd.isnull(df.iat[row-1,column])):

        print("Título da coluna: " + str(cell))
        print("Valores: ")
    else:
        print(str(cell))
