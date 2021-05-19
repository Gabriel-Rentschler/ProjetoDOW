import pandas as pd

def Extremidades(row, column, df):
   
    ampRow, ampColumn = 0, 0

    if(row==0):
        ampRow = 1
    elif(row==df.shape[0]):
        ampRow = -1

    if(column==0):
        ampColumn = 1
    elif(column==df.shape[1]):
        ampColumn = -1

    return ampRow, ampColumn

def lePlanilha(cell, df, row, column):

    ampRow, ampColumn = Extremidades(row, column, df)

    if(row==0 or pd.isnull(df.iat[row-1,column])):

        print("Título da coluna: " + str(cell))
        print("Valores: ")
    else:
        print(str(cell))
