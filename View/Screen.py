import os
from tokenize import String
from tkinter import *
from tkinter import ttk
from tkinter import tix
from tkinter import messagebox
from reportlab.lib.pagesizes import letter, A4
from Models.Pedido import Pedido
from Relatorios.relatorio import Relatorios
from Services.DBManager import DBManager
from Services.criptografia import Criptografia

main_path = os.path.dirname(__file__)

# logo = PhotoImage(file=main_path+'\bow.png')


class Validacao:
    def null(self, text):
        if text == "":
            return True
        try:
            value = int(text)
        except ValueError:
            return False
        return value <= 100000000000


class Screen(Relatorios,  Validacao, Criptografia):

    def __init__(self):
        # criando a janela
        self.janela = tix.Tk()
        self.janela.title('Login da aplicação')
        self.janela.geometry('310x300')
        self.janela.config(background="#f0f3f5")
        self.janela.resizable(width=False, height=False)
        self.dBManager = DBManager()

        self.dict_senhas()
        self.InitializeFrames()
        self.InitializeFrameAbove()
        self.InitializeFrameBelow()

        self.janela.mainloop()

    def pedidoSelected(self):

        codigo = self.input_codProduto.get()
        data = self.input_dataCompra.get()
        quantity = self.input_qtdProduto.get()
        describe = self.input_descProduto.get("1.0", END)

        self.pedidoSeleted = Pedido(codigo, data, quantity, describe)

    def Intialize(self):
        self.tela()
        self.frames()
        self.botoes()
        self.labels_frame1()
        self.labels_frame2()
        self.pedidoSelected()

    def limpar(self):
        # Limpar interface
        self.input_codProduto.delete(0, END)
        self.input_dataCompra.delete(0, END)
        self.input_qtdProduto.delete(0, END)
        self.input_descProduto.delete("1.0", END)

    def adicionar(self):

        self.pedidoSelected()

        if self.pedidoSeleted.codigo == "":

            msg = "O cadastro de pedido só irá ser realizado\n"
            msg += "com o preenchimento do campo cod_Produto."
            messagebox.showinfo("Erro de cadastro!", msg)

        else:

            # Add Pedido ao Banco de Dados
            self.pedidoSelected()
            self.dbManager.Add(self.pedidoSeleted)

            msg3 = "O cadastro do pedido foi adicionado."
            messagebox.showinfo("Cadastro!", msg3)

            self.select_lista()
            self.limpar()

    def select_lista(self):

        self.lista_Pedidos.delete(*self.lista_Pedidos.get_children())

        listaDb = self.dbManager.ReadAll()

        for pedido in listaDb:
            self.lista_Pedidos.insert("", END, values=pedido)

    def duploclick(self, event):

        self.limpar()

        self.lista_Pedidos.selection()

        for n in self.lista_Pedidos.selection():

            col1, col2, col3, col4 = self.lista_Pedidos.item(n, 'values')

            self.pedidoSeleted = Pedido(col1, col2, col3, col4)

            self.input_codProduto.insert(END, col1)
            self.input_dataCompra.insert(END, col2)
            self.input_qtdProduto.insert(END, col3)
            self.input_descProduto.insert(END, col4)

    def deletarpaciente(self):
        if self.tipo_login(self.e_nome.get()):

            self.pedidoSelected()
            self.dbManager.Delete(self.pedidoSeleted)

            msg1 = "O pedido foi apagado."
            messagebox.showinfo("Cadastro", msg1)

            self.limpar()
            self.select_lista()

        elif self.input_codProduto.get() == "":

            messagebox.showinfo(
                "Erro", "Campo Código vazio. Dê um doubleclick para selecionar um pedido.")

            return
        else:
            messagebox.showinfo(
                "Erro", "Você não tem previlegios administrativos.")

            return

    def alterarPedido(self):
        if self.tipo_login(self.e_nome.get()):
            self.pedidoSelected()
            self.dbManager.Update(self.pedidoSeleted)

            msg2 = "O cadastro do pedido foi alterado."
            messagebox.showinfo("Cadastro", msg2)

            self.select_lista()
            self.limpar()
        elif self.input_codProduto.get() == "":
            messagebox.showinfo(
                "Erro", "Campo Código vazio. Dê um doubleclick para selecionar um pedido.")

            return

        else:
            messagebox.showinfo(
                "Erro", "Você não tem previlegios administrativos.")

            return

    def buscar(self):

        self.lista_Pedidos.delete(*self.lista_Pedidos.get_children())

        self.input_dataCompra.insert(END, '%')

        if self.cod_Produto == "":

            msg4 = "Preencha o campo do codigo."
            messagebox.showinfo("Cadastro", msg4)

        else:

            codigo = self.input_codProduto.get()

            result = self.dbManager.Read(codigo)

            for i in result:
                self.lista_Pedidos.insert("", END, values=i)

        self.limpar()

    def validarCOD(self):
        self.cod_var = (self.janela2.register(self.null), "%P")

    def tela(self):

        self.xWindows = 1280
        self.yWindows = 720
        self.title = "SISTEMA DE PEDIDOS"
        self.janela2.title(self.title)

        self.janela2.configure(background='#46295a')

        self.janela2.geometry(f'{self.xWindows}x{self.yWindows}')

        self.janela2.resizable(True, True)

        self.janela2.maxsize(width=1920, height=1080)

        self.janela2.minsize(width=550, height=380)

        self.janela2.iconbitmap(main_path, 'bow.ico')

    def frames(self):

        self.frame1 = Frame(self.janela2, bd=4, bg='#F0F8FF',

                            highlightbackground='black', highlightthickness=4)

        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.45, relheight=0.96)

        self.frame2 = Frame(self.janela2, bd=4, bg='#BEBEBE',

                            highlightbackground='black', highlightthickness=3)

        self.frame2.place(relx=0.49, rely=0.02, relwidth=0.5, relheight=0.96)

    def botoes(self):
        # Buscar
        self.bt_buscar = Button(self.frame1, text='Buscar', bd=3, bg='#836FFF', fg='black', font=(
            'candara', 12, 'bold'), command=self.buscar)
        self.bt_buscar.place(relx=0.02, rely=0.9,
                             relwidth=0.09, relheight=0.05)

        # limpar
        self.bt_limpar = Button(self.frame1, text='Limpar', fg='black', font=(
            'candara', 12, 'bold'), command=self.limpar)
        self.bt_limpar.place(relx=0.14, rely=0.9, relwidth=0.1, relheight=0.05)

        # alterar
        self.bt_alterar = Button(self.frame1, text='Alterar', bd=3, bg='#FFDEAD', fg='black', font=(
            'candara', 12, 'bold'), command=self.alterarPedido)
        self.bt_alterar.place(relx=0.25, rely=0.9,
                              relwidth=0.1, relheight=0.05)

        # apagar
        self.bt_apagar = Button(self.frame1, text='Apagar', bd=3, bg='#A0522D', fg='black', font=(
            'candara', 12, 'bold'), command=self.deletarpaciente)
        self.bt_apagar.place(relx=0.4, rely=0.9, relwidth=0.1, relheight=0.05)

        # adicionar
        self.bt_add = Button(self.frame1, text='Adicionar', bd=3, bg='#66CDAA', fg='black', font=(
            'candara', 12, 'bold'), command=self.adicionar)
        self.bt_add.place(relx=0.53, rely=0.9, relwidth=0.13, relheight=0.05)

    def labels_frame1(self):

        # Codigo do pedido
        self.cod_Produto = Label(
            self.frame1, text='Codigo do pedido', bg='#F0F8FF', font=('candara', 10, 'bold'))
        self.cod_Produto.place(relx=0.38, rely=0.1)
        self.input_codProduto = Entry(
            self.frame1, validate="key", validatecommand=self.cod_var)
        self.input_codProduto.place(relx=0.07, rely=0.1)

        # data_Compra
        self.data_Compra = Label(
            self.frame1, text='Data da compra do pedido', bg='#F0F8FF', font=('candara', 10, 'bold'))
        self.data_Compra.place(relx=0.38, rely=0.2)
        self.input_dataCompra = Entry(self.frame1)
        self.input_dataCompra.place(relx=0.07, rely=0.2)

        # Quantidade de produtos
        self.qtd_Produto = Label(
            self.frame1, text='Quantidade de produtos', bg='#F0F8FF', font=('candara', 10, 'bold'))
        self.qtd_Produto.place(relx=0.38, rely=0.3)
        self.input_qtdProduto = Entry(
            self.frame1, validate="key", validatecommand=self.cod_var)
        self.input_qtdProduto.place(relx=0.07, rely=0.3)

        # Desc Produtos
        self.desc_Produto = Label(
            self.frame1, text='Descrição do produto', bg='#F0F8FF', font=('candara', 10, 'bold'))
        self.desc_Produto.place(relx=0.55, rely=0.4)
        self.input_descProduto = Text(self.frame1)
        self.input_descProduto.place(
            relx=0.07, rely=0.4, relwidth=0.45, relheight=0.18)

        # Balões de mensagem
        self.ba_buscar = tix.Balloon(self.frame1)
        self.ba_buscar.bind_widget(
            self.bt_buscar, balloonmsg="Clique para buscar pelo número do pedido.")

        self.ba_limpar = tix.Balloon(self.frame1)
        self.ba_limpar.bind_widget(
            self.bt_limpar, balloonmsg="Clique para preencher novamente o formulário.")

        self.ba_alterar = tix.Balloon(self.frame1)
        self.ba_alterar.bind_widget(
            self.bt_alterar, balloonmsg="Clique para alterar os dados do pedido, o codigo do pedido não pode ser alterado!.")

        self.ba_apagar = tix.Balloon(self.frame1)
        self.ba_apagar.bind_widget(
            self.bt_apagar, balloonmsg="Clique para apagar os dados do pedido.")

        self.ba_adicionar = tix.Balloon(self.frame1)
        self.ba_adicionar.bind_widget(
            self.bt_add, balloonmsg="Preencha os dados do pedido e clique em adicionar.")

        # logo imagem
        # self.logo = Label(janela2, image= logo, bg='#F0F8FF')
        # self.logo.place(relx=0.64, rely= 0.075)

        # sobre
        self.sobre = Label(self.frame1, text='ALPHABET', fg='black',
                           bg='#F0F8FF', font=('candara', 12, 'bold'))
        self.sobre.place(relx=0.69, rely=0.8)

    def labels_frame2(self):
        self.lista_Pedidos = ttk.Treeview(
            self.frame2, height=3, columns=('col1', 'col2', 'col3', 'col4'))
        # cabeçario
        self.lista_Pedidos.heading('#0', text="")
        self.lista_Pedidos.heading('#1', text="Código de produto")
        self.lista_Pedidos.heading('#2', text="data de compra")
        self.lista_Pedidos.heading('#3', text="Quantidade")
        self.lista_Pedidos.heading('#4', text="Descrição do produto")

        # colunas
        self.lista_Pedidos.column('#0', width=0)
        self.lista_Pedidos.column('#1', width=50)
        self.lista_Pedidos.column('#2', width=50)
        self.lista_Pedidos.column('#3', width=50)
        self.lista_Pedidos.column('#4', width=100)

        # criaçao
        self.lista_Pedidos.place(relx=0.01, rely=0.01,
                                 relwidth=0.95, relheight=0.85)

        # barra de rolagem
        self.barra_rolagem = Scrollbar(self.frame2, orient='vertical')
        self.lista_Pedidos.configure(yscroll=self.barra_rolagem.set)
        self.barra_rolagem.place(relx=0.96, rely=0.01,
                                 relwidth=0.04, relheight=0.85)
        self.lista_Pedidos.bind("<Double-1>", self.duploclick)

    def menus(self):
        menubar = Menu(self.janela2)
        self.janela2.config(menu=menubar)
        menu1 = Menu(menubar)
        menu2 = Menu(menubar)

        def Quit(): self.janela2.destroy()

        menubar.add_cascade(label="Opções", menu=menu1)
        menubar.add_cascade(label="Exportar", menu=menu2)

        menu1.add_command(label="Atualizar", command=self.select_lista)
        menu1.add_command(label="Sair", command=Quit)
        menu2.add_command(label="Gerar relatório", command=self.geraRel)

    def InitializeFrames(self):
        # Dividindo a janela

        self.frame_cima = Frame(self.janela, width=310,
                                height=50, bg="#f0f3f5", relief='flat')
        self.frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

        self.frame_baixo = Frame(
            self.janela, width=310, height=250, bg="#FF7F50", relief='flat')
        self.frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

    def InitializeFrameAbove(self):

        # Configurando o frame de cima
        self.l_nome = Label(self.frame_cima, text='Login', anchor=NE, font=(
            'Ivy 25'), bg="#f0f3f5", fg='#000000')
        self.l_nome.place(x=5, y=5)

        self.l_linha = Label(self.frame_cima, text='', width=275,  anchor=NW, font=(
            'Ivy 1'), bg="#f0f3f5", fg='#000000')
        self.l_linha.place(x=10, y=45)

    def InitializeFrameBelow(self):
        # Configurando o frame de baixo
        self.l_nome = Label(self.frame_baixo, text='Nome *',
                            anchor=NW, font=('Ivy 10'), bg="#f0f3f5", fg='#000000')
        self.l_nome.place(x=10, y=20)
        self.e_nome = Entry(self.frame_baixo, width=25, justify='left', font=(
            '', 15), highlightthickness=1, relief='solid')
        self.e_nome.place(x=14, y=50)

        self.l_pass = Label(self.frame_baixo, text='Senha *',
                            anchor=NW, font=('Ivy 10'), bg="#f0f3f5", fg='#000000')
        self.l_pass.place(x=10, y=95)
        self.e_pass = Entry(self.frame_baixo, width=25, justify='left',
                            show='*', font=('', 15), highlightthickness=1, relief='solid')
        self.e_pass.place(x=14, y=130)

        self.b_confirmar = Button(self.frame_baixo, command=self.Entrar, text='Confirmar', width=39, height=2, font=(
            'Ivy 8 bold'), bg="#f0f3f5", fg='#000000', relief=RAISED, overrelief=RIDGE)
        self.b_confirmar.place(x=15, y=180)

    def Entrar(self):

        if self.login(self.e_nome.get(), self.e_pass.get()):

            messagebox.showinfo(
                'login', 'Seja bem Vindo(a)!')
            self.nova_janela()

        else:
            messagebox.showwarning(
                'Erro', 'Verifique o nome e a senha do usuário')

    def nova_janela(self):
        self.janela.geometry('0x0')
        self.janela2 = Toplevel()
        self.dbManager = DBManager()
        self.dbManager.Initialize()

        self.validarCOD()
        self.Intialize()
        self.select_lista()
        self.menus()

        self.janela2.mainloop()
