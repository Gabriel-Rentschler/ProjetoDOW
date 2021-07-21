import pandas as pd
import sys
import readSheet, planilha

path = sys.argv[1]
listaPlanilha=[]

def LerPlanilha():
    xl = pd.ExcelFile(path)
    numSheets = len(xl.sheet_names)

    for sheets in range(numSheets):
        df = pd.read_excel(path, sheet_name=sheets, header=None)
        newPlanilha = planilha.Planilha(xl.sheet_names[sheets], df.shape[0], df.shape[1])
        listaPlanilha.append(newPlanilha)
        listaPlanilha[sheets].CriarTabela(df)

LerPlanilha()
listaPlanilha[0].listaTabela[0].MostraValores()
print(listaPlanilha)
print()
print(listaPlanilha[0].listaTabela)
print(listaPlanilha[1].listaTabela)
print()
listaPlanilha[1].listaTabela[0].MostraValores()
print()
print(listaPlanilha[0].listaTabela[0].linhas)
print(listaPlanilha[0].listaTabela[0].colunas)
