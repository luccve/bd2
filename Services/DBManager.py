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

        #criando tabelas
        self.cursor.execute("""
            CREATE SEQUENCE IF NOT EXISTS pedidos_id_seq INCREMENT 1;
        """)

        self.conection.commit();         
        print('Create sequence')

        self.desconectarbd()

    def CreateTables(self):

        self.conectarbd()

        #criando tabelas
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS pedidos (
                cod_Produto INTEGER PRIMARY KEY NOT NULL DEFAULT nextval('pedidos_id_seq'::regclass),
                data_Compra DATE,
                qtd_Produto INTEGER,
                desc_Produto CHARACTER VARYING(80)
            );
        """)

        self.conection.commit();         
        print('Tables Criadas')

        self.desconectarbd()

    def conectarbd(self):
        # IMPLEMENTAR O SGBDEXTERNO

        self.conection = psycopg2.connect(f"dbname=postgres user={self.user} password={self.password} host={self.host} port={self.port}")

        self.cursor = self.conection.cursor(); 

        print("Conectando ao banco de dados")

    def desconectarbd(self):

        self.conection.close(); 
        print("Banco de dados desconectado")

    def CreateViewPedidos(self):

        self.conectarbd()

        self.cursor.execute("""CREATE OR REPLACE VIEW ultimos_pedidos as SELECT cod_Produto, data_Compra, qtd_Produto, desc_Produto
                    FROM pedidos ORDER BY data_Compra ASC; """)    
        
        self.conection.commit()

        self.desconectarbd()           

    def Add(self, pedido):

        self.conectarbd()

        query = '''INSERT INTO pedidos (data_compra, qtd_produto, desc_produto)            
                VALUES (%s,%s,%s)'''                

        self.cursor.execute(query, (pedido.date, pedido.quantity, pedido.describe))

        self.conection.commit()

        self.desconectarbd()
            
    def Update(self, pedido):

        self.conectarbd()

        self.cursor.execute(""" UPDATE pedidos SET  cod_Produto = ?, data_Compra = ?, qtd_Produto = ?, desc_Produto = ? 
            WHERE cod_Produto=? """, (pedido.codigo, pedido.date, pedido.quantity, pedido.describe, pedido.codigo))

        self.conection.commit()
        self.desconectarbd()

    def Read(self, codigo):

        self.conectarbd()
        
        lista = self.cursor.execute(
            """ SELECT * FROM pedidos WHERE cod_Produto =? """ , codigo)   

        return lista

    def ReadAll(self):

        self.conectarbd()

        lista = self.cursor.execute("select * from ultimos_pedidos ")    

        lista = self.cursor.fetchall()

        return lista

    def Delete(self, pedido):

        self.conectarbd()

        self.cursor.execute(
            """ DELETE FROM pedidos WHERE cod_Produto = ? """, [pedido.codigo])

        self.conection.commit()
        self.desconectarbd()

    def loginDatabase(self,user,password,host="localhost",port="5432"):

        self.GetDataLogin()
 
        self.conection = psycopg2.connect(f"dbname=postgres user={self.user} password={self.password} host={self.host} port={self.port}")

        self.cursor = self.conection.cursor(); 

        return True

        





