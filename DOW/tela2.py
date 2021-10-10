from tkinter import *
import main

def tela(listaPlanilha):

    tela = Tk()


    tela.title("--- Nome Projeto ---")


    bt1 = Button(tela, width=25,height=3, text="Gerar Grafico Pizza", background= "#6B7DFA", foreground="#fff", relief=GROOVE, command=lambda : main.gerarGrafico(listaPlanilha, 2))
    bt1.place(x=540, y=325)
    bt2 = Button(tela, width=25,height=3, text="Gerar Gráfico em Coluna", background= "#6B7DFA", foreground="#fff", relief=GROOVE, command=lambda : main.gerarGrafico(listaPlanilha, 1))
    bt2.place(x=540, y=450)
    bt3 = Button(tela, width=25,height=3, text="Gerar Gráfico em Linha", background= "#6B7DFA", foreground="#fff", relief=GROOVE, command=lambda : main.gerarGrafico(listaPlanilha, 0))
    bt3.place(x=540, y=210)

    bt4 = Button(tela, width=15,height=3, text="Selecionar Y", background= "#6B7DFA", foreground="#fff", relief=GROOVE)
    bt4.place(x=630, y=35)
    bt5 = Button(tela, width=15,height=3, text="Selecionar X", background= "#6B7DFA", foreground="#fff", relief=GROOVE)
    bt5.place(x=470, y=35)

    tela.geometry("800x600+450+125")
    tela.wm_resizable(width=False, height=False)

    tela.mainloop()