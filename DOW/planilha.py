import pandas as pd
import readSheet, tabela

class Planilha:
    #Inicialização do objeto planilha
    def __init__(self, nome, linhas, colunas):
        self.nome = nome
        self.linhas = linhas
        self.colunas = colunas
        self.listaTabela = []

    #Função de gerar tabelas
    def CriarTabela(self, df):
        tabelaCriada=False
        tabelaLinha={}

        #Para cada linha o programa verifica todas as colunas da planilha e as coloca em tabelaLinha.
        
        for row in range(1, df.shape[0]):
            tabelaColuna={}
            linhaVazia=True

            for column in range(df.shape[1]):
                
                #Se na linha inteira tiver ao menos uma célula com dados, ela deixa de estar vazia
                if pd.notnull(df.iat[row, column]):
                    linhaVazia=False
                
                tabelaColuna[df.iat[0,column]] = df.iat[row,column]

            #Se a linha estiver vazia e nenhuma tabela estiver criada, ele cria uma nova tabela.
            #Isso evita se tiver duas lihas vazias consecutivas para não criar uma tabela em branco.
            if linhaVazia==True and tabelaCriada==False:
                newTabela = tabela.Tabela('Tabela', len(tabelaLinha), len(tabelaLinha[0]), tabelaLinha)
                self.listaTabela.append(newTabela)

                tabelaLinha={}
                tabelaCriada=True
            elif linhaVazia==False:
                tabelaLinha[row-1] = tabelaColuna
                tabelaCriada=False
        #Quando terminar o número de linhas o programa checa mais uma vez se não há alguma informação acumulada nas colunas.
        if tabelaLinha!={}:
            newTabela = tabela.Tabela('Tabela', len(tabelaLinha), len(tabelaLinha[0]), tabelaLinha)
            self.listaTabela.append(newTabela)