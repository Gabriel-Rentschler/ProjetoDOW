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
        tabelaColuna=[]
        tabelaLinha=[]

        #Para cada linha o programa verifica todas as colunas da planilha e as coloca em tabelaLinha.
        
        for row in range(self.linhas):
            tabelaLinha=[]
            linhaVazia=True

            for column in range(self.colunas):
                cell = df.iat[row, column]
                
                #Se na linha inteira tiver ao menos uma célula com dados, ela deixa de estar vazia
                if pd.notnull(cell):
                    linhaVazia=False
                
                tabelaLinha.append(cell)

            #Se a linha estiver vazia e nenhuma tabela estiver criada, ele cria uma nova tabela.
            #Isso evita se tiver duas lihas vazias consecutivas para não criar uma tabela em branco.
            if linhaVazia==True and tabelaCriada==False:
                newTabela = tabela.Tabela('Tabela', len(tabelaColuna), len(tabelaColuna[0]), tabelaColuna)
                self.listaTabela.append(newTabela)

                tabelaColuna=[]
                tabelaCriada=True
            elif linhaVazia==False:    
                tabelaColuna.append(tabelaLinha)
                tabelaCriada=False
        #Quando terminar o número de linhas o programa checa mais uma vez se não há alguma informação acumulada nas colunas.
        if tabelaColuna!=[]:
            newTabela = tabela.Tabela('Tabela', len(tabelaColuna), len(tabelaColuna[0]), tabelaColuna)
            self.listaTabela.append(newTabela)