from ast import Try
from msilib.schema import Error
from Models.Pedido import Pedido
import psycopg2
from tkinter import messagebox

USER = "postgres"
PASSWORD = "root"
HOST = "localhost"
PORT = "5432"


class DBManager:

    def __init__(self):

        self.GetDataLogin()

    def GetDataLogin(self):

        self.user = USER
        self.password = PASSWORD
        self.host = HOST
        self.port = PORT

    def Initialize(self):

        self.CreateSequence()
        self.CreateTables()
        self.CreateViewPedidos()

    def CreateSequence(self):
        self.conectarbd()

        # criando tabelas
        self.cursor.execute("""
            CREATE SEQUENCE IF NOT EXISTS pedidos_id_seq INCREMENT 1;
        """)

        self.conection.commit()
        print('Create sequence')

        self.desconectarbd()

    def CreateTables(self):

        self.conectarbd()

        # criando tabelas
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS pedidos (
                cod_Produto INTEGER PRIMARY KEY NOT NULL DEFAULT nextval('pedidos_id_seq'::regclass),
                data_Compra DATE CHECK (data_Compra > '2022-01-01 00:00:00'),
                qtd_Produto INTEGER CHECK (qtd_Produto >= 0),
                desc_Produto CHARACTER VARYING(80)
            );
        """)

        self.conection.commit()
        print('Tables Criadas')

        self.desconectarbd()

    def conectarbd(self):
        # IMPLEMENTAR O SGBDEXTERNO

        try:
            self.conection = psycopg2.connect(
                f"dbname=postgres user={self.user} password={self.password} host={self.host} port={self.port}")

            self.cursor = self.conection.cursor()

            print("Banco de dados Conectado")

        except Exception as e:

            print(f'Erro na conexão com o banco de dados: {e}')

    def desconectarbd(self):

        try:

            self.conection.close()
            print("Banco de dados desconectado")

        except Exception as e:

            print(f'Erro ao desconectar banco de dados: {e}')

    def CreateViewPedidos(self):

        try:
            self.conectarbd()
            self.cursor.execute("""CREATE OR REPLACE VIEW ultimos_pedidos as SELECT cod_Produto, data_Compra, qtd_Produto, desc_Produto
                        FROM pedidos ORDER BY data_Compra ASC; """)

            self.conection.commit()

            print("View ultimos_pedidos criada")

        except Exception as e:

            print(f'Erro em CreateViewPedidos: {e}')

        finally:
            self.desconectarbd()

    def Add(self, pedido):

        try:

            self.conectarbd()

            query = '''INSERT INTO pedidos (data_compra, qtd_produto, desc_produto)            
                    VALUES (CURRENT_TIMESTAMP,%s,%s)'''

            self.cursor.execute(
                query, (pedido.quantity, pedido.describe))

            self.conection.commit()

        except Exception as e:

            messagebox.showwarning(
                'Erro', f' Não é possível adicinar esse pedido: {e}')

        finally:

            self.desconectarbd()

    def Update(self, pedido):

        try:
            self.conectarbd()

            # Controle de Concorrência
            comand = f"""LOCK TABLE pedidos IN ROW EXCLUSIVE  MODE; UPDATE pedidos SET data_compra = '{pedido.date}', qtd_Produto = {pedido.quantity}, desc_Produto = '{pedido.describe}' WHERE cod_Produto = {pedido.codigo}"""

            self.cursor.execute(comand)

            self.conection.commit()

        except Exception as e:

            messagebox.showwarning(
                'Erro', f'Em atualizar pedidos verifique há um pedido selecionado.')

        finally:

            self.desconectarbd()

    def Read(self, codigo):

        try:

            self.conectarbd()

            lista = self.cursor.execute(
                f""" SELECT * FROM pedidos WHERE cod_Produto = {codigo} """)

            lista = self.cursor.fetchall()

            return lista

        except Exception as e:

            messagebox.showwarning(
                'Erro', f'Erro ao ler o pedido de cod: {codigo}')

        finally:

            self.desconectarbd()

    def ReadAll(self):

        try:

            self.conectarbd()

            lista = self.cursor.execute("select * from ultimos_pedidos ")

            lista = self.cursor.fetchall()

            return lista

        except Exception as e:

            messagebox.showwarning(
                'Erro', f'A consulta a pedidps está indiponível no momento')

        finally:

            self.cursor.close()

    def Delete(self, pedido):

        try:

            self.conectarbd()

            self.cursor.execute(
                f"""LOCK TABLE pedidos IN ROW EXCLUSIVE  MODE; DELETE FROM pedidos WHERE cod_Produto = {pedido.codigo}""")

            self.conection.commit()

        except Exception as e:

            messagebox.showwarning(
                'Erro', f'Não foi possível deletar o pedido cod: {pedido.codigo}')

        finally:

            self.desconectarbd()
