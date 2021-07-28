import pandas as pd
import planilha

#Função para apresentar os dados de uma planilha de forma organizada para a API ler em seguida.
def lePlanilha(planilha):

    print("Planilha: " + planilha.nome)
    print("Linhas: " + str(planilha.listaTabela[0].linhas))
    print("Colunas: " + str(planilha.listaTabela[0].colunas))

    for col in range(0, planilha.listaTabela[0].colunas):

        print("Título da coluna: " + planilha.listaTabela[0].valores[0][col])
        print("Valores: ")
        for lin in range(1, planilha.listaTabela[0].linhas):

            print(planilha.listaTabela[0].valores[lin][col])
