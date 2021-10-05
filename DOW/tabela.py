class Tabela:
    #Inicialização do objeto tabela
    def __init__(self, titulo, linhas, colunas, valores):
        self.titulo = titulo
        self.linhas = linhas
        self.colunas = colunas
        self.valores = valores

    #Uma função de debug, mostra os valores na tabela
    def MostraValores(self):
        for col in range(self.colunas):
            text=[]
            for lin in range(self.linhas):
                text.append(self.valores[col][lin])

            print(text)

    def mostraColuna(self, col):
        text = []
        for lin in range(1, self.linhas):
            text.append(self.valores[lin][col])

        return text
