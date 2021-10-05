import pandas as pd
import matplotlib.pyplot as plt

class Grafico():
    def __init__(self, titulo, x, y):
        self.titulo = titulo
        self.x = x
        self.y = y

    def CriarGrafico(self, tabela):
        print('Título: ')
        print(self.titulo)

        print('Eixo X: ')
        self.x = tabela.mostraColuna(self.x)
        print(self.x)
        print('eixo Y: ')
        self.y = tabela.mostraColuna(self.y)
        print(self.y)

        dataframe = {'Col1': self.x,
                     'Col2': self.y}

        var_df = pd.DataFrame(dataframe, columns=['Col1', 'Col2'])

        var_df.plot.bar(x='Col1', y='Col2')
        plt.show()
        