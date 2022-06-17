
if __name__ == "__main__":
    try:
        import os
        import webbrowser
        import sqlite3
        from tkinter import *
        from tkinter import ttk
        from tkinter import tix
        from tkinter import messagebox
        from h11 import ERROR
        from reportlab.pdfgen import canvas
        from reportlab.lib.pagesizes import letter, A4
        from textwrap import wrap
        from relatorio import Relatorios
        from funcoes import Funcoes
    except ValueError:
        print ("voce tem alguma biblioteca nao instalada")
    finally:
        from pedidos import Layout
        Layout()
    
