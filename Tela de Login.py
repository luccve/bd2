from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox


# criando a janela
janela = Tk()
janela.title('')
janela.geometry('310x300')
janela.config(background="#f0f3f5")
janela.resizable(width=False, height=False)

# Dividindo a janela

frame_cima = Frame(janela, width=310, height=50, bg="#f0f3f5", relief='flat')
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width=310, height=250, bg="#FF7F50", relief='flat')
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# Configurando o frame de cima
l_nome = Label(frame_cima, text='Login', anchor=NE, font=('Ivy 25'), bg="#f0f3f5", fg='#000000')
l_nome.place(x=5, y=5)

l_linha = Label(frame_cima, text='', width=275,  anchor=NW, font=('Ivy 1'), bg="#f0f3f5", fg='#000000')
l_linha.place(x=10, y=45)

credenciais = [['Ana','123456'],['Bruno','123456']]

def verificar_senha():
    nome = e_nome.get()
    senha = e_pass.get()

    if nome == 'admin' and senha == 'admin':
        messagebox.showinfo('Login', 'Seja bem Vindo Admin!')
    elif credenciais[0] == nome and credenciais[1] == senha:
        messagebox.showinfo('Login', 'Seja bem Vindo(a) ,' + credenciais[0])
        # deletar itens presentes no frame baixo e cima
        for widget in frame_baixo.winfo_children():
            widget.destroy()
        for widget in frame_cima.winfo_children():
            widget.destroy()

        nova_janela()

    else:
        messagebox.showwarning('Erro','Verifique o nome e a senha do usuário')

#funcao apos verificacao
def nova_janela():
    #configurando o frame acima
    l_nome = Label(frame_cima, text='Usuário : ' + credenciais[0] , anchor=NE, font=('Ivy 20'), bg="#f0f3f5", fg='#000000')
    l_nome.place(x=5, y=5)

    l_linha = Label(frame_cima, text='', width=275, anchor=NW, font=('Ivy 1'), bg="#f0f3f5", fg='#000000')
    l_linha.place(x=10, y=45)

    l_nome = Label(frame_baixo, text='Seja bem vindo ' + credenciais[0], anchor=NE, font=('Ivy 20'), bg="#f0f3f5", fg='#000000')
    l_nome.place(x=5, y=105)




# Configurando o frame de baixo
l_nome = Label(frame_baixo, text='Nome *', anchor=NW, font=('Ivy 10'), bg="#f0f3f5", fg='#000000')
l_nome.place(x=10, y=20)
e_nome = Entry(frame_baixo, width=25, justify='left', font=('',15),highlightthickness=1,relief='solid')
e_nome.place(x=14,y=50)

l_pass = Label(frame_baixo, text='Senha *', anchor=NW, font=('Ivy 10'), bg="#f0f3f5", fg='#000000')
l_pass.place(x=10, y=95)
e_pass = Entry(frame_baixo, width=25, justify='left', show='*',font=('',15),highlightthickness=1,relief='solid')
e_pass.place(x=14,y=130)

b_confirmar = Button(frame_baixo, command=verificar_senha, text='Confirmar', width=39, height=2, font=('Ivy 8 bold'), bg="#f0f3f5", fg='#000000', relief=RAISED,overrelief=RIDGE)
b_confirmar.place(x=15, y=180)




janela.mainloop()

