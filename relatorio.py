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
from funcoes import Funcoes



class Relatorios(Event, Funcoes):
    def abrirPdf(self):
        self.id_p = self.input_codProduto.get()+"_pedido.pdf" 
        
        webbrowser.open(self.id_p)
    def geraRel(self):
        self.pedidosRelatorio = canvas.Canvas(self.input_codProduto.get()+"_pedido.pdf")

        self.codPedido = self.input_codProduto.get()        
        self.dataCompra = self.input_dataCompra.get()   
        self.qtdProduto = self.input_qtdProduto.get()   
        self.descPedido = self.input_descProduto.get("1.0", "end-1c")   
        
     
        
        self.pedidosRelatorio.setFont("Helvetica-Bold", 24)
        self.pedidosRelatorio.drawString(200, 790, 'Ficha do Paciente')

        self.pedidosRelatorio.setFont("Helvetica-Bold", 14)
        self.pedidosRelatorio.drawString(50, 700, 'Código do pedido: ')
        self.pedidosRelatorio.drawString(50, 670, 'Data da compra: ')
        self.pedidosRelatorio.drawString(50, 640, 'Quantidade do produto: ')
        self.pedidosRelatorio.drawString(50, 610, 'Descrição do pedido: ')
       
        self.pedidosRelatorio.setFont("Helvetica-Bold", 8)
        self.pedidosRelatorio.drawString(270, 100, 'Açai do tevinho')
        self.pedidosRelatorio.drawString(150,45,'Rua Governador Dix Sept Rosado, Campo Grande, Recife - PE - CEP 52031010')
        self.pedidosRelatorio.drawString(230, 60, 'O açai mais gostoso da região')
        

        self.pedidosRelatorio.setFont("Helvetica", 11)
        self.pedidosRelatorio.drawString(250, 700, self.codPedido)
        self.pedidosRelatorio.line(50,690,500,690)
        self.pedidosRelatorio.drawString(250, 670, self.dataCompra)
        self.pedidosRelatorio.line(50,660,500,660)
        self.pedidosRelatorio.drawString(250, 640, self.qtdProduto)
        self.pedidosRelatorio.line(50,630,500,630)
        self.pedidosRelatorio.drawString(250, 610, self.descPedido)
        self.pedidosRelatorio.line(50,600,500,600)
        
        
        # b = wrap(self.desc_Produto, 90)
        # print(b)
        # text = self.pedidosRelatorio.beginText(40, 200)
        # for l in b:
        #     text.textLine(l)
        # self.pedidosRelatorio.drawText(text)

        self.pedidosRelatorio.drawImage("bow.png",50,60,width=60, height=63, mask=[255,255,255])
        # self.pedidosRelatorio.rect(20, 30, 555, 270, fill= False, stroke=True)
        # 

        self.pedidosRelatorio.showPage()
        self.pedidosRelatorio.save()
        self.abrirPdf()


