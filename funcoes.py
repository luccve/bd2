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



class Funcoes():
    
    def limpar(self):
        #Limpar interface
        self.input_codProduto.delete(0, END)
        self.input_dataCompra.delete(0, END)
        self.input_qtdProduto.delete(0, END)
        self.input_descProduto.delete("1.0", END)
        
        

    def conectarbd(self):
        # IMPLEMENTAR O SGBDEXTERNO
        
        self.conectar = sqlite3.connect("pedidos.db")
        self.cursor = self.conectar.cursor(); print("Conectando ao banco de dados")
    
    def desconectarbd(self):
        self.conectar.close(); print("Banco de dados desconectado")

    def addPedido(self):
        self.conectarbd()
        #criando tabelas
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS pedidos (
                cod_Produto INTERGER PRIMARY KEY,
                data_Compra DATE,
                qtd_Produto INTERGER,
                desc_Produto text

            );
        """)

        self.conectar.commit(); print('Banco de dados criado')
        self.desconectarbd()

    def variaveis(self):
        
        self.cod_Produto = self.input_codProduto.get()
        self.data_Compra = self.input_dataCompra.get()
        self.qtd_Produto = self.input_qtdProduto.get()
        self.desc_Produto = self.input_descProduto.get("1.0", "end-1c")
     

    def adicionar(self):
        
        self.variaveis()
        #condição de preenchimento do cpf e nome do paciente com mensagem de erro
        if self.cod_Produto == "":
            msg = "O cadastro de pedido só irá ser realizado\n"
            msg+= "com o preenchimento do campo cod_Produto."
            messagebox.showinfo("Erro de cadastro!", msg)
            
        else:
            self.parametros = (self.cod_Produto, self.data_Compra, self.qtd_Produto, self.desc_Produto)

            self.conectarbd()
            self.cursor.execute(""" INSERT INTO pedidos (cod_Produto, data_Compra, qtd_Produto, desc_Produto)            
                VALUES (?,?,?,?)""", (self.parametros))
            self.conectar.commit()

            msg3 = "O cadastro do pedido foi adicionado."
            messagebox.showinfo("Cadastro!", msg3)

            self.desconectarbd()
            self.select_lista()
            self.limpar()

    def select_lista(self):
        self.lista_Pedidos.delete(*self.lista_Pedidos.get_children())
        self.conectarbd()

        lista = self.cursor.execute("""SELECT cod_Produto, data_Compra, qtd_Produto, desc_Produto
                    FROM pedidos ORDER BY data_Compra ASC; """)
        
        for i in lista:
            self.lista_Pedidos.insert("", END, values= i)
        
        self.desconectarbd()

    def duploclick(self, event):
        self.limpar()
        self.lista_Pedidos.selection()
        for n in self.lista_Pedidos.selection():
            col1, col2, col3, col4 = self.lista_Pedidos.item(n, 'values')
            self.input_codProduto.insert(END, col1)
            self.input_dataCompra.insert(END, col2)
            self.input_qtdProduto.insert(END, col3)
            self.input_descProduto.insert(END, col4)
          

    def deletarpaciente(self):
        self.variaveis()
        self.conectarbd()
        self.cursor.execute(""" DELETE FROM pedidos WHERE cod_Produto = ? """, [self.cod_Produto])
        self.conectar.commit()
        msg1 = "O pedido foi apagado."
        messagebox.showinfo("Cadastro", msg1)

        self.desconectarbd()
        self.limpar()
        self.select_lista()

    def alterarPedido(self):
        self.variaveis()
        self.conectarbd()

        self.cursor.execute(""" UPDATE pedidos SET  cod_Produto = ?, data_Compra = ?, qtd_Produto = ?, desc_Produto = ? 
            WHERE cod_Produto=? """, (self.cod_Produto, self.data_Compra, self.qtd_Produto, self.desc_Produto, self.cod_Produto))

        self.conectar.commit()

        msg2 = "O cadastro do pedido foi alterado."
        messagebox.showinfo("Cadastro", msg2)

        self.desconectarbd()
        self.select_lista()
        self.limpar()

    def buscar(self):
        self.variaveis()
        self.conectarbd()
        self.lista_Pedidos.delete(*self.lista_Pedidos.get_children())

        self.input_dataCompra.insert(END, '%')

        if self.cod_Produto == "":
            msg4 = "Preencha o campo do codigo."
            messagebox.showinfo("Cadastro", msg4)

        else:
            nome = self.input_dataCompra.get()
            self.cursor.execute(
                """ SELECT self.cod_Produto, self.data_Compra, self.qtd_Produto, self.desc_Produto
                        FROM pedidos WHERE data_Compras LIKE '%s'  ORDER BY data_Compras ASC  """ % nome)
            
            buscarnome = self.cursor.fetchall()

            for i in buscarnome:
                self.lista_Pedidos.insert("", END, values = i)
        
        self.limpar()
        
        self.desconectarbd()