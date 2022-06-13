import os
import webbrowser
import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import tix
from tkinter import messagebox
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from textwrap import wrap
from relatorio import Relatorios
from funcoes import Funcoes


main_path = os.path.dirname(__file__)

janela = tix.Tk()
#logo = PhotoImage(file=main_path+'\bow.png')


class Validacao:
    def null(self, text):
        if text == "": return True
        try:
            value = int(text)
        except ValueError:
            return False
        return value <=100000000000



class Prontuario(Funcoes, Relatorios, Validacao):

    def __init__(self):

        
        self.janela = janela
        self.validarCOD()
        self.tela()
        self.frames()
        self.botoes()
        self.labels_frame1()
        self.labels_frame2()
        self.addPedido()
        self.select_lista()
        self.menus()

        janela.mainloop()

    def tela(self):
        self.xWindows = 1280
        self.yWindows = 720
        self.title = "SISTEMA DE PEDIDOS"
        self.janela.title(self.title)

        self.janela.configure(background= '#46295a')
        
        self.janela.geometry(f'{self.xWindows}x{self.yWindows}')

        self.janela.resizable(True, True)

        self.janela.maxsize(width= 1920, height= 1080)

        self.janela.minsize(width=550, height=380)
        
        self.janela.iconbitmap(main_path,'bow.ico')

    def frames(self):

        self.frame1 = Frame(self.janela, bd = 4, bg = '#F0F8FF',

                            highlightbackground= 'black', highlightthickness=4 )

        self.frame1.place(relx= 0.02 , rely=0.02, relwidth= 0.45,relheight= 0.96)



        self.frame2 = Frame(self.janela, bd=4, bg='#BEBEBE',

                            highlightbackground='black', highlightthickness=3)

        self.frame2.place(relx=0.49, rely=0.02, relwidth=0.5, relheight=0.96)
    
    def botoes(self):
        #Buscar
        self.bt_buscar = Button(self.frame1, text= 'Buscar', bd= 3, bg= '#836FFF', fg= 'black'
                                ,font=('candara', 12, 'bold' ), command=self.buscar)
        self.bt_buscar.place(relx= 0.02, rely= 0.9, relwidth=0.09, relheight=0.05)
        
        #limpar
        self.bt_limpar = Button(self.frame1, text= 'Limpar', fg= 'black'
                                ,font=('candara', 12, 'bold' ), command= self.limpar)
        self.bt_limpar.place(relx= 0.14, rely= 0.9, relwidth=0.1, relheight=0.05)

        #alterar
        self.bt_alterar = Button(self.frame1, text= 'Alterar', bd=3, bg='#FFDEAD', fg= 'black'
                                ,font=('candara', 12, 'bold' ), command=self.alterarPedido)
        self.bt_alterar.place(relx= 0.25, rely= 0.9, relwidth=0.1, relheight=0.05)

        #apagar
        self.bt_apagar = Button(self.frame1, text= 'Apagar', bd=3, bg ='#A0522D', fg= 'black'
                                ,font=('candara', 12, 'bold' ), command=self.deletarpaciente)
        self.bt_apagar.place(relx= 0.4, rely= 0.9, relwidth=0.1, relheight=0.05)

        #adicionar
        self.bt_add = Button(self.frame1, text= 'Adicionar', bd=3, bg='#66CDAA', fg= 'black'
                                ,font=('candara', 12, 'bold' ), command=self.adicionar)
        self.bt_add.place(relx= 0.53, rely= 0.9, relwidth=0.13, relheight=0.05)
    
    def labels_frame1(self):

        #Codigo do pedido
        self.cod_Produto = Label(self.frame1, text='Codigo do pedido',bg='#F0F8FF' , font=('candara', 10 ,'bold'))
        self.cod_Produto.place(relx= 0.38, rely= 0.1)
        self.input_codProduto = Entry(self.frame1, validate="key", validatecommand=self.cod_var)
        self.input_codProduto.place(relx= 0.07, rely= 0.1)
        
        #data_Compra
        self.data_Compra = Label(self.frame1, text='Data da compra do pedido',bg='#F0F8FF' , font=('candara', 10 ,'bold'))
        self.data_Compra.place(relx= 0.38, rely= 0.2)
        self.input_dataCompra = Entry(self.frame1)
        self.input_dataCompra.place(relx= 0.07, rely= 0.2)

        #Quantidade de produtos
        self.qtd_Produto = Label(self.frame1, text='Quantidade de produtos',bg='#F0F8FF' , font=('candara', 10 ,'bold'))
        self.qtd_Produto.place(relx= 0.38, rely= 0.3)
        self.input_qtdProduto = Entry(self.frame1)
        self.input_qtdProduto.place(relx= 0.07, rely= 0.3)

        #Desc Produtos
        self.desc_Produto = Label(self.frame1, text='Descrição do produto',bg='#F0F8FF' , font=('candara', 10 ,'bold'))
        self.desc_Produto.place(relx= 0.55, rely= 0.4)
        self.input_descProduto = Text(self.frame1)
        self.input_descProduto.place(relx= 0.07, rely= 0.4, relwidth=0.45, relheight=0.18)

        

        #Balões de mensagem
        self.ba_buscar = tix.Balloon(self.frame1)
        self.ba_buscar.bind_widget(self.bt_buscar, balloonmsg = "Clique para buscar pelo número do pedido.")

        self.ba_limpar = tix.Balloon(self.frame1)
        self.ba_limpar.bind_widget(self.bt_limpar, balloonmsg = "Clique para preencher novamente o formulário.")

        self.ba_alterar = tix.Balloon(self.frame1)
        self.ba_alterar.bind_widget(self.bt_alterar, balloonmsg = "Clique para alterar os dados do pedido, o codigo do pedido não pode ser alterado!.")
        
        self.ba_apagar = tix.Balloon(self.frame1)
        self.ba_apagar.bind_widget(self.bt_apagar, balloonmsg = "Clique para apagar os dados do pedido.")

        self.ba_adicionar = tix.Balloon(self.frame1)
        self.ba_adicionar.bind_widget(self.bt_add, balloonmsg = "Preencha os dados do pedido e clique em adicionar.")

        
        #logo imagem
        #self.logo = Label(janela, image= logo, bg='#F0F8FF')
        #self.logo.place(relx=0.64, rely= 0.075)
        
        #sobre
        self.sobre = Label(self.frame1, text='ALPHABET', fg= 'black', bg='#F0F8FF', font=('candara', 12 ,'bold'))
        self.sobre.place(relx= 0.69, rely= 0.8)

    def labels_frame2(self):
        self.lista_Pedidos= ttk.Treeview(self.frame2, height=3, columns=('col1', 'col2', 'col3', 'col4'))
        #cabeçario
        self.lista_Pedidos.heading('#0', text="Código de produto")
        self.lista_Pedidos.heading('#1', text="data de compra")
        self.lista_Pedidos.heading('#2', text="Quantidade")
        self.lista_Pedidos.heading('#3', text="Descrição do produto")
       

        #colunas
        self.lista_Pedidos.column('#0', width=150)
        self.lista_Pedidos.column('#1', width=150)
        self.lista_Pedidos.column('#2', width=100)
        self.lista_Pedidos.column('#3', width=200)
    

        #criaçao
        self.lista_Pedidos.place(relx=0.01, rely=0.01, relwidth=0.95, relheight=0.85)

        #barra de rolagem
        self.barra_rolagem = Scrollbar(self.frame2, orient='vertical')
        self.lista_Pedidos.configure(yscroll=self.barra_rolagem.set)
        self.barra_rolagem.place(relx= 0.96 , rely= 0.01, relwidth= 0.04, relheight= 0.85)
        self.lista_Pedidos.bind("<Double-1>", self.duploclick)

    def menus(self):
        menubar = Menu(self.janela)
        self.janela.config(menu=menubar)
        menu1 = Menu(menubar)
        menu2 = Menu(menubar) 

        def Quit(): self.janela.destroy()
        
        menubar.add_cascade(label="Opções", menu = menu1)
        menubar.add_cascade(label="Exportar", menu = menu2)

        menu1.add_command(label="Sair", command=Quit)
        menu2.add_command(label="Gerar relatório", command=self.geraRel)

    def validarCOD(self):
        self.cod_var = (self.janela.register(self.null), "%P")
    

Prontuario()