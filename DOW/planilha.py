class Planilha:
    def __init__(self, nome, linhas, colunas):
        self.nome = nome
        self.linhas = linhas
        self.colunas = colunas

    def CriarTabela():
        tabelaColuna=[]
        tabelaLinha=tabelaColuna[:]

        for column in range(colunas):
            for row in range(linhas):
                cell = df.iat[row, column]

                if pd.notnull(cell):
                    
