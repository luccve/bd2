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



class Relatorios(Event):
    def abrirPdf(self):
        self.id_p = self.input_codProduto.get()+"_pedido.pdf" 
        
        webbrowser.open(self.id_p)
    def geraRel(self):
        self.pacienteRel = canvas.Canvas(self.input_codProduto.get()+"_pedido.pdf")

        self.cpfRel = self.input_codProduto.get()        
        self.nomeRel = self.input_dataCompra.get()   
        self.dataRel = self.input_qtdProduto.get()   
        self.comoRel = self.input_descProduto.get("1.0", "end-1c")   
        self.remRel = self.remedio_input.get("1.0", "end-1c")   
     
        
        self.pacienteRel.setFont("Helvetica-Bold", 24)
        self.pacienteRel.drawString(200, 790, 'Ficha do Paciente')

        self.pacienteRel.setFont("Helvetica-Bold", 14)
        self.pacienteRel.drawString(50, 700, 'CPF: ')
        self.pacienteRel.drawString(50, 670, 'Nome: ')
        self.pacienteRel.drawString(50, 640, 'Data de Nascimento: ')
        self.pacienteRel.drawString(50, 610, 'Comorbidades: ')
        self.pacienteRel.drawString(50, 580, 'Medicações de uso continúo: ')
        self.pacienteRel.drawString(50, 550, 'Alergia Medicamentosa: ')
        self.pacienteRel.drawString(50, 520, 'Sinais Vitais: ')
        self.pacienteRel.drawString(50, 490, 'Evolução Médica: ')
        self.pacienteRel.drawString(50, 400, 'Conduta: ')      
        self.pacienteRel.setFont("Helvetica-Bold", 8)
        self.pacienteRel.drawString(240, 60, 'Dr. Fabian Morais/CRM-PE 15 170')
        self.pacienteRel.drawString(150,45,'Rua Governador Dix Sept Rosado, Campo Grande, Recife - PE - CEP 52031010')
        self.pacienteRel.drawString(230, 250, 'Receituário Médico: ')
        

        self.pacienteRel.setFont("Helvetica", 11)
        self.pacienteRel.drawString(90, 701, self.cpfRel)
        self.pacienteRel.drawString(100, 670, self.nomeRel)
        self.pacienteRel.drawString(200, 640, self.dataRel)
        self.pacienteRel.drawString(160, 610, self.comoRel)
        self.pacienteRel.drawString(250, 580, self.remRel)
        self.pacienteRel.drawString(220, 550, self.alerRel)
        self.pacienteRel.drawString(150, 520, self.sinRel)
        self.pacienteRel.drawString(50, 470, self.evoRel)
        self.pacienteRel.drawString(50, 380, self.condRel)
        
        b = wrap(self.recRel, 90)
        print(b)
        text = self.pacienteRel.beginText(40, 200)
        for l in b:
            text.textLine(l)
        self.pacienteRel.drawText(text)

       # self.pacienteRel.drawImage("bow.png",50,60,width=60, height=63, mask=[255,255,255])
        self.pacienteRel.rect(20, 30, 555, 270, fill= False, stroke=True)
        self.pacienteRel.line(220,70,400,70)

        self.pacienteRel.showPage()
        self.pacienteRel.save()
        self.abrirPdf()


