import pandas as pd
import matplotlib.pyplot as plt
from xlsxwriter import *

class Grafico():
    def __init__(self, titulo, x, y):
        self.titulo = titulo
        self.x = x
        self.y = y

    def CriarGrafico(self, tabela, tipoGrafico):
        print('Título: ')
        print(self.titulo)

        print('Eixo X: ')
        xTitulo = self.x
        self.x = tabela.mostraColuna(self.x)
        print('------------------')
        print(self.x)
        print('eixo Y: ')
        yTitulo = self.y
        self.y = tabela.mostraColuna(self.y)
        print('------------------')
        print(self.y)

        dataframe = {xTitulo: self.x,
                     yTitulo: self.y}

        var_df = pd.DataFrame(dataframe)

        #Salvar arquivo
        excel_file = 'output.xlsx'
        sheet_name = 'Data set'
        writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')
        var_df.to_excel(writer, sheet_name=sheet_name)

        workbook = writer.book
        worksheet = writer.sheets[sheet_name]

        if tipoGrafico == 0:
            #var_df.plot.line(x=xTitulo, y=yTitulo)
            chart = workbook.add_chart({'type': 'line'})
        elif tipoGrafico == 1:
            #var_df.plot.bar(x=xTitulo, y=yTitulo)
            chart = workbook.add_chart({'type': 'bar'})
        else:
            #var_df.plot.pie(x=xTitulo, y=yTitulo)
            chart = workbook.add_chart({'type': 'pie'})

        max_row = len(var_df)
        col_x = var_df.columns.get_loc(xTitulo) + 1
        col_y = var_df.columns.get_loc(yTitulo) + 1

        chart.add_series({
            'name':       xTitulo + " por " + yTitulo,
            'categories': [sheet_name, 1, col_x, max_row, col_x],
            'values':     [sheet_name, 1, col_y, max_row, col_y],
        })

        chart.set_x_axis({'name': xTitulo})
        chart.set_y_axis({'name': yTitulo,
                          'major_gridlines': {'visible': False}})

        worksheet.insert_chart('D2', chart)
        writer.save()
        #plt.show()
        