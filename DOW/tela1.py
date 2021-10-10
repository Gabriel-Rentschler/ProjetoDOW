from tkinter import *
from tkintertable import TableCanvas, TableModel
from tkintertable.Testing import sampledata
import tkinter.filedialog as fd
import os, sys, main, tela2

listaPlanilha=[]
data = sampledata()
print(data)

master = Tk()

def carregaArquivo():
    currdir = os.getcwd()
    path = fd.askopenfilename(parent=master, initialdir=currdir, title='Selecione o arquivo de planilha')
    main.LerPlanilha(listaPlanilha, path)

def mostrarTabela(selPlanilha):
    if selPlanilha == 1:
        tframe = Frame(master)
        tframe.pack(side='left')
        table = TableCanvas(tframe,
                            cellwidth=60, cellbackgr='#e3f698',
                            thefont=('Arial',12),rowheight=18, rowheaderwidth=30,
                            rowselectedcolor='yellow', editable=False, data=data)
        table.show()

master.title("--- Nome Projeto ---")

bt = Button(master, width=40,height=4, text="Carregar Arquivo",  background= "#6B7DFA", foreground="#fff", 
relief=GROOVE, command=lambda : carregaArquivo())
bt.place(x=280, y=480)

bt1 = Button(master, width=25,height=3, text="Gerar Tabela", background= "#6B7DFA", foreground="#fff", 
relief=GROOVE, command=lambda : main.lerTabela(listaPlanilha))
bt1.place(x=540, y=325)

bt2 = Button(master, width=25,height=3, text="Gerar Gráfico", background= "#6B7DFA", foreground="#fff", 
relief=GROOVE, command=lambda : tela2.tela(listaPlanilha))
bt2.place(x=540, y=210)

bt3 = Button(master, width=10,height=3, text="Planiha 1", background= "#6B7DFA", foreground="#fff", 
relief=GROOVE, command=lambda : mostrarTabela(1))
bt3.place(x=680, y=35)
bt4 = Button(master, width=10,height=3, text="Planiha 2", background= "#6B7DFA", foreground="#fff", relief=GROOVE)
bt4.place(x=580, y=35)
bt5 = Button(master, width=10,height=3, text="Planiha 3", background= "#6B7DFA", foreground="#fff", relief=GROOVE)
bt5.place(x=480, y=35)

master.geometry("800x600+450+125")
master.wm_resizable(width=False, height=False)

master.mainloop()
