import pandas as pd

def Formatacao():

def lePlanilha(cell, df, row, column):  

    if(row==0):
        Formatacao(1, 0)
    else if(row==df.shape[0]):
        Formatacao(-1, 0)

    if(column==0):
        Formatacao(0, 1)
    else if(column==df.shape[1]):
        Formatacao(0, -1)

    if(row<df.shape[0]-1 and column<df.shape[1]-1 and row > 0 and column >0):
        if(pd.isnull(df.iat[row+1,column]) and pd.isnull(df.iat[row-1,column]) and pd.isnull(df.iat[row,column+1]) and pd.isnull(df.iat[row,column-1])):
            print("Título da tabela:")

    print(str(cell) + ' | ', end = '')


