from tkinter import *


master = Tk()


master.title("--- Nome Projeto ---")

bt = Button(master, width=40,height=4, text="Carregar Arquivo",  background= "#6B7DFA", foreground="#fff", relief=GROOVE)
bt.place(x=280, y=480)
bt1 = Button(master, width=25,height=3, text="Gerar Tabela", background= "#6B7DFA", foreground="#fff", relief=GROOVE)
bt1.place(x=540, y=325)
bt2 = Button(master, width=25,height=3, text="Gerar Gráfico", background= "#6B7DFA", foreground="#fff", relief=GROOVE)
bt2.place(x=540, y=210)

bt3 = Button(master, width=10,height=3, text="Planiha 3", background= "#6B7DFA", foreground="#fff", relief=GROOVE)
bt3.place(x=680, y=35)
bt4 = Button(master, width=10,height=3, text="Planiha 2", background= "#6B7DFA", foreground="#fff", relief=GROOVE)
bt4.place(x=580, y=35)
bt5 = Button(master, width=10,height=3, text="Planiha 3", background= "#6B7DFA", foreground="#fff", relief=GROOVE)
bt5.place(x=480, y=35)

master.geometry("800x600+450+125")
master.wm_resizable(width=False, height=False)

master.mainloop()
