import pandas as pd
import readSheet

class Planilha:

    def __init__(self, nome, linhas, colunas):
        self.nome = nome
        self.linhas = linhas
        self.colunas = colunas

    listaTabela=[]

    def CriarTabela(self, df):
        print('Tabela 1 da planilha ' + self.nome)

        tabelaColuna=[]
        tabelaLinha=tabelaColuna[:]

        for column in range(self.colunas):
            for row in range(self.linhas):
                cell = df.iat[row, column]

                if pd.notnull(cell):
                    readSheet.lePlanilha(cell, df, row, column)
