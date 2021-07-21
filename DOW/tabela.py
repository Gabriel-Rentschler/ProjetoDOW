class Tabela:

    def __init__(self, titulo, linhas, colunas, valores):
        self.titulo = titulo
        self.linhas = linhas
        self.colunas = colunas
        self.valores = valores

    def MostraValores(self):
        for col in range(self.colunas):
            text=[]
            for lin in range(self.linhas):
                text.append(self.valores[col][lin])

            print(text)
