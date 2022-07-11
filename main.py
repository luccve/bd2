
if __name__ == "__main__":
    try:
        from View.ScreenLogin import ScreenLogin
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
        from Relatorios.relatorio import Relatorios

        from View.Screen import Screen

    except ValueError:

        print("voce tem alguma biblioteca nao instalada")

    finally:
        Screen()
