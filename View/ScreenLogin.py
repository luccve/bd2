from tkinter import *
from tkinter import Tk, ttk, tix
from tkinter import messagebox
from Services.DBManager import DBManager
from View.Screen import Screen
from hashlib import md5


class ScreenLogin():

    def __init__(self):

        # criando a janela
        self.janela = tix.Tk()
        self.janela.title('')
        self.janela.geometry('310x300')
        self.janela.config(background="#f0f3f5")
        self.janela.resizable(width=False, height=False)
        self.dBManager = DBManager()

        self.dict_senhas()
        self.InitializeFrames()
        self.InitializeFrameAbove()
        self.InitializeFrameBelow()

        self.janela.mainloop()

    def dict_senhas(self):
        self.users = {"admin": ["admin", "202cb962ac59075b964b07152d234b70"], "user": [
            "user", "202cb962ac59075b964b07152d234b70"]}

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

        self.credenciais = [['Ana', '123456'], ['Bruno', '123456']]

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

    def dict_senhas(self):
        self.users = {"admin": ["admin", "202cb962ac59075b964b07152d234b70"], "user": [
            "user", "202cb962ac59075b964b07152d234b70"]}

    def login(self, nome, senha):
        if nome == "" or senha == "":
            return False

        else:
            self.senha = md5(senha.encode('utf8')).hexdigest()
            for s in self.users.values():
                if s[1] == self.senha:
                    return True
                else:
                    return False

    def tipo_login(self):
        self.nome = self.e_nome.get()

    def nova_janela(self):

        Screen()
