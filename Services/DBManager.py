from Models.Pedido import Pedido
import sqlite3


class DBManager:        

    def conectarbd(self):
        # IMPLEMENTAR O SGBDEXTERNO

        self.conectionDatabase = sqlite3.connect("pedidos.db")
        self.cursor = self.conectionDatabase.cursor(); 

        print("Conectando ao banco de dados")

    def desconectarbd(self):

        self.conectionDatabase.close(); 
        print("Banco de dados desconectado")

    def CreateTables(self):

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

        self.conectionDatabase.commit();         
        print('Tables Criadas')

        self.desconectarbd()

    def Create(self, pedido):

        self.conectarbd()

        self.cursor.execute(""" INSERT INTO pedidos (cod_Produto, data_Compra, qtd_Produto, desc_Produto)            
                VALUES (?,?,?,?)""", (pedido.codigo, pedido.date, pedido.quantity, pedido.describe))

        self.conectionDatabase.commit()

        self.desconectarbd()
            
    def Update(self, pedido):

        self.conectarbd()

        self.cursor.execute(""" UPDATE pedidos SET  cod_Produto = ?, data_Compra = ?, qtd_Produto = ?, desc_Produto = ? 
            WHERE cod_Produto=? """, (pedido.codigo, pedido.date, pedido.quantity, pedido.describe, pedido.codigo))

        self.conectionDatabase.commit()
        self.desconectarbd()

    def Read(self, codigo):

        self.conectarbd()
        
        lista = self.cursor.execute(
            """ SELECT * FROM pedidos WHERE cod_Produto =? """ , codigo)   

        return lista

    def ReadAll(self):

        self.conectarbd()

        lista = self.cursor.execute("""SELECT cod_Produto, data_Compra, qtd_Produto, desc_Produto
                    FROM pedidos ORDER BY data_Compra ASC; """)    
    
        return lista

    def Delete(self, pedido):

        self.conectarbd()

        self.cursor.execute(
            """ DELETE FROM pedidos WHERE cod_Produto = ? """, [pedido.codigo])

        self.conectionDatabase.commit()
        self.desconectarbd()



