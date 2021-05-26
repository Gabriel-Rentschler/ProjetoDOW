import pandas as pd
import readSheet, tabela

class Planilha:

    def __init__(self, nome, linhas, colunas):
        self.nome = nome
        self.linhas = linhas
        self.colunas = colunas
        self.listaTabela = []

    def CriarTabela(self, df):
        print('Tabela 1 da planilha ' + self.nome)

        tabelaColuna=[]
        tabelaLinha=[]

        for column in range(self.colunas):
            tabelaLinha=[]

            for row in range(self.linhas):
                cell = df.iat[row, column]

                if pd.notnull(cell):
                    tabelaLinha.append(cell)
                    #readSheet.lePlanilha(cell, df, row, column)
            
            if tabelaLinha==[]:
                newTabela = tabela.Tabela('Tabela', len(tabelaColuna), len(tabelaColuna), tabelaColuna)
                self.listaTabela.append(newTabela)

                tabelaColuna=[]
            else:    
                tabelaColuna.append(tabelaLinha)

        newTabela = tabela.Tabela('Tabela', len(tabelaColuna), len(tabelaColuna), tabelaColuna)
        self.listaTabela.append(newTabela)
        print(self.listaTabela)
