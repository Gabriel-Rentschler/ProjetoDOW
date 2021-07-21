import pandas as pd
import readSheet, tabela

class Planilha:

    def __init__(self, nome, linhas, colunas):
        self.nome = nome
        self.linhas = linhas
        self.colunas = colunas
        self.listaTabela = []

    def CriarTabela(self, df):

        tabelaCriada=False
        tabelaColuna=[]
        tabelaLinha=[]

        for column in range(self.colunas):
            tabelaLinha=[]

            for row in range(self.linhas):
                cell = df.iat[row, column]

                tabelaLinha.append(cell)
                #readSheet.lePlanilha(cell, df, row, column)

            if pd.isnull(tabelaLinha[0]) and tabelaCriada==False:
                newTabela = tabela.Tabela('Tabela', len(tabelaColuna[0]), len(tabelaColuna), tabelaColuna)
                self.listaTabela.append(newTabela)

                tabelaColuna=[]
                tabelaCriada=True
            elif pd.notnull(tabelaLinha[0]):    
                tabelaColuna.append(tabelaLinha)
                tabelaCriada=False
        if tabelaColuna!=[]:
            newTabela = tabela.Tabela('Tabela', len(tabelaColuna[0]), len(tabelaColuna), tabelaColuna)
            self.listaTabela.append(newTabela)