import pandas as pd
import sys
import readSheet, planilha

path = sys.argv[1]
planilha=[]

def LerPlanilha():
    xl = pd.ExcelFile(path)
    numSheets = len(xl.sheet_names)

    for sheets in range(numSheets):
        df = pd.read_excel(path, sheet_name=sheets, header=None)
        planilha.append(planilha.Planilha(xl.sheet_names[sheets], df.shape[0], df.shape[1]))
        planilha.CriarTabela()

        for column in range(df.shape[1]):
            for row in range(df[sheets].shape[0]):
                cell = df[sheets].iat[row, column]

                if pd.notnull(df[sheets].iat[row, column]):
                    readSheet.lePlanilha(cell, df[sheets], row, column)

def PrintarPlanilha():

    for sheets in range(numSheets):
        print(df)
        res = input("Print sheet?")
        if res == "n":
            break
        if res == "y":
            df.append(pd.read_excel(path, sheet_name = sheets, header=None))
            print('')
            print('Nome da planilha: %s' %xl.sheet_names[sheets])

        for column in range(df[sheets].shape[1]):
            for row in range(df[sheets].shape[0]):
                cell = df[sheets].iat[row, column]

                if pd.notnull(df[sheets].iat[row, column]):
                    readSheet.lePlanilha(cell, df[sheets], row, column)

            print('')

LerPlanilha()
