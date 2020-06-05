from tkinter import *

root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames()
        self.widgets()
        self.root.mainloop()
    def tela(self):
        self.root.title("Receitas manuais - RfZorzi")
        self.root.configure(background= "lightgray");
        self.root.geometry("1000x600")
        self.root.resizable(TRUE, TRUE);
        self.root.minsize(width=800, height=500)
        self.root.maxsize(width=1200, height=900)
    def frames(self):
        ###     Primeiro Container da janela
        top = Frame(self.root, bd=2, bg="#3a5e9c", highlightbackground='gray65', highlightthickness=1, relief = 'ridge')
        top.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.1)
        self.top = top
        ###     Segundo Container da janela
        top2 = Frame(self.root, bd=2, bg='#3a5e9c', highlightbackground='gray65', highlightthickness=1, relief = 'ridge')
        top2.place(relx=0.52, rely=0.16, relwidth=0.46, relheight=0.1)
        self.top2 = top2
        ###     Terceiro Container da janela
        top3 = Frame(self.root, bd=2, bg='white', highlightbackground='gray65', highlightthickness=1, relief = 'ridge')
        top3.place(relx=0.02, rely=0.26, relwidth=0.96, relheight=0.5)
        self.top3 = top3
        ###     Quarto Container da janela
        top4 = Frame(self.root, bd=2, bg='#3a5e9c', highlightbackground='gray65', highlightthickness=1, relief = 'ridge')
        top4.place(relx=0.02, rely=0.78, relwidth=0.96, relheight=0.2)
        self.top = top
    def widgets(self):
        self.lb_entrada = Label(self.top, text='Entrada', bg='#3a5e9c', fg='white').place(relx= 0.05, rely=0.05)
        self.inp_entrada = Entry(self.top, fg='gray35').place(relx=0.05, rely=0.5, relwidth= 0.07)

        self.lb_saida = Label(self.top, text='Saida', bg='#3a5e9c', fg='white').place(relx=0.15, rely=0.05)
        self.inp_saida = Entry(self.top, fg='gray35').place(relx=0.15, rely=0.5, relwidth=0.07)

        self.lb_dia = Label(self.top, text = 'Dia', bg='#3a5e9c', fg='white').place(relx=0.35, rely=0.05)
        self.inp_dia = Entry(self.top, fg='gray35').place(relx=0.35, rely=0.5, relwidth=0.04)

        self.lb_mes = Label(self.top, text = 'Mês', bg='#3a5e9c', fg='white').place(relx=0.4, rely=0.05)
        self.inp_mes = Entry(self.top, fg='gray35').place(relx=0.4, rely=0.5, relwidth=0.04)

        self.lb_ano = Label(self.top, text = 'Ano', bg='#3a5e9c', fg='white').place(relx=0.45, rely=0.05)
        self.inp_ano = Entry(self.top, fg='gray35').place(relx=0.45, rely=0.5, relwidth=0.07)

        self.lb_obs = Label(self.top, text = 'Obs:', bg='#3a5e9c', fg='white').place(relx=0.55, rely=0.05)
        self.inp_obs = Entry(self.top, fg='gray35').place(relx=0.55, rely=0.5, relwidth=0.3)

        self.bt_inserir = Button(self.top, text= 'Inserir', bg= "white",bd = 1, highlightbackground='gray65',
                    highlightthickness=1, fg="#2859b8", font=('verdana', 11, 'bold')).place(relx=0.9, rely=0.2)
        #####
        self.mes_listaLb = Label(self.top2, text= 'Mês', bg= 'gray', fg= 'lightgray',
                                 font=('Verdana', '7', 'bold'))
        self.mes_listaLb.place(relx=0.1, rely=0.19, relwidth=0.2, relheight=0.62)
        self.mesListaEntry = Frame(self.top2, bd=2)
        self.mesListaEntry.grid(column=0, row=0, sticky=(N, W, E, S))
        self.mesListaEntry.columnconfigure(0, weight=1)
        self.mesListaEntry.rowconfigure(0, weight=1)
        self.mesListaEntry.place(relx=0.1, rely=0.1, relwidth=0.3, relheight=0.9)
        self.corvar = StringVar(self.top2)
        self.coresV = {'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro',
                       'Outubro', 'Novembro', 'Dezembro'}
        self.corvar.set('Junho')
        self.popupMenu = OptionMenu(self.mesListaEntry, self.corvar, *self.coresV)
        self.popupMenu.grid(row=2, column=1)

        self.mesListaEntry.place(relx=0.1, rely=0.2, relwidth=0.2, relheight=0.6)

        self.ano_listaLb = Label(self.top2, text='Mês', bg='gray', fg='lightgray',
                                 font=('Verdana', '7', 'bold'))
        self.ano_listaLb.place(relx=0.4, rely=0.19, relwidth=0.15, relheight=0.62)
        self.anoListaEntry = Frame(self.top2, bd=2)
        self.anoListaEntry.grid(column=0, row=0, sticky=(N, W, E, S))
        self.anoListaEntry.columnconfigure(0, weight=1)
        self.anoListaEntry.rowconfigure(0, weight=1)
        self.anoListaEntry.place(relx=0.4, rely=0.1, relwidth=0.2, relheight=0.9)
        self.corvar2 = StringVar(self.top2)
        self.coresV2 = {'2020', '2021', '2022'}
        self.corvar2.set('2020')
        self.popupMenu = OptionMenu(self.anoListaEntry, self.corvar2, *self.coresV2)
        self.popupMenu.grid(row=2, column=1)

        self.anoListaEntry.place(relx=0.4, rely=0.2, relwidth=0.18, relheight=0.64)





Application()