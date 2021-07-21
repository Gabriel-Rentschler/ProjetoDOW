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
        linhaVazia=True

        for row in range(self.linhas):
            tabelaLinha=[]

            for column in range(self.colunas):
                cell = df.iat[row, column]

                if pd.notnull(cell):
                    linhaVazia=False

                tabelaLinha.append(cell)
                #readSheet.lePlanilha(cell, df, row, column)

            if linhaVazia==True and tabelaCriada==False:
                newTabela = tabela.Tabela('Tabela', len(tabelaColuna[0]), len(tabelaColuna), tabelaColuna)
                self.listaTabela.append(newTabela)

                tabelaColuna=[]
                tabelaCriada=True
            elif linhaVazia==False:    
                tabelaColuna.append(tabelaLinha)
                tabelaCriada=False
        if tabelaColuna!=[]:
            newTabela = tabela.Tabela('Tabela', len(tabelaColuna[0]), len(tabelaColuna), tabelaColuna)
            self.listaTabela.append(newTabela)