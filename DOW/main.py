import pandas as pd
import sys
import readSheet, planilha, grafico, textoparafala

#sys.argv se refere aos argumentos passados na hora de rodar o programa. No caso o caminho do arquivo excel a ser lido está no primeiro argumento.
#Ex.: python3 pdmain.py tabelastest/tables2.xlsx
#               ^                  ^
#             sys.argv[0]      sys.argv[1]


#Função para guardar a lista de planilhas de tabelas. Lê todo o arquivo e guarda no programa.
def LerPlanilha(listaPlanilha, path):
    #Abre o arquivo excel
    xl = pd.ExcelFile(path)
    #Guarda número de planilhas que tem dentro do arquivo
    numSheets = len(xl.sheet_names)

    #Para cada planilha no arquivo excel coloca-se a planilha dentro da listaPlanilha
    for sheets in range(numSheets):
        df = pd.read_excel(path, sheet_name=sheets, header=None)
        #Criação de um novo objeto planilha
        newPlanilha = planilha.Planilha(xl.sheet_names[sheets], df.shape[0], df.shape[1])
        #Coloca o objeto planilha na listaPlanilha e executa a função de criar tabelas para a planilha
        listaPlanilha.append(newPlanilha)
        listaPlanilha[sheets].CriarTabela(df)

def lerTabela(listaPlanilha):
    try:
        readSheet.lePlanilha(listaPlanilha[0])
    except Exception:
        print('')
    #textoparafala.CriarAudio(listaPlanilha[0].listaTabela[0].valores[0][0])

def gerarGrafico(listaPlanilha, tipoGrafico):
    newgrafico = grafico.Grafico(listaPlanilha[0].listaTabela[0].valores[0][0] + ' por ' + listaPlanilha[0].listaTabela[0].valores[0][1], 0, 1)
    newgrafico.CriarGrafico(listaPlanilha[0].listaTabela[0], tipoGrafico)