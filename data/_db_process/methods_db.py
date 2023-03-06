import connector
import secrets

#criação e inserção de dados no DB
class methods():
    #insere qualquer valor na tabela de usuário
    def insert_user(self, column, value, where, id):
        mydb = connector.connect()
        mycursor = mydb.cursor()
        try:
            sql = "UPDATE users_ SET %s = %s WHERE %s = %s;"
            val = (column, value, where, id)
            mycursor.execute(sql, val)
            mydb.commit()
        except mydb.Error as err:
            return None, err.errno
        finally:
            mydb.close()
        return mycursor.rowcount, "record inserted."
    

    #insere qualquer valor na tabela de business
    def insert_business(self, column, value, where, id):
        mydb = connector.connect()
        mycursor = mydb.cursor()
        try:
            sql = "UPDATE users_ SET %s = %s WHERE %s = %s;"
            val = (column, value, where, id)
            mycursor.execute(sql, val)
            mydb.commit()

        except mydb.connector.Error as err:
            return None, err.errno
        finally:
            mydb.close()
        return mycursor.rowcount, "record inserted."


    #insere usuário padrão
    def create_user(self, x1, x2, x3, x4):
        mydb = connector.connect()
        mycursor = mydb.cursor()
        try:
            sql = "INSERT INTO users_ (username, email, password, registertimestamp) VALUES (%s, %s, %s, %s)"
            val = (f"{x1}", f"{x2}", f"{x3}", x4)
            mycursor.execute(sql, val)
            mydb.commit()
        except mydb.Error as err:
            return None, err.errno
        finally:
            mydb.close()
        return mycursor.rowcount, "record inserted."
    

    #insere e cria business ao usuário
    def create_business(self, x1, x2, x3):
        mydb = connector.connect()
        mycursor = mydb.cursor()
        try:
            businessid = secrets.token_urlsafe(8)
            sql = "INSERT INTO business_ (businessid, businessname, ownerid, registertimestamp) VALUES (%s, %s, %s, %s)"
            val = (businessid, f"{x1}", x2, x3)
            mycursor.execute(sql, val)
            mydb.commit()

        except mydb.Error as err:
            return None, err.errno
        finally:
            mydb.close()
        return mycursor.rowcount, "record inserted."
    
set = methods()

result, code = set.create_user("break20001", "vinicius12", "vini@rafa", 2134566666)
business = set.create_business("Tecnosync.br", 44, 2312421323)
