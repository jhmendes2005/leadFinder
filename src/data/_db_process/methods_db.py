import secrets
import mysql.connector
import json


#obtém as informações do DB
with open('./data/_security/host.json', 'r') as f:
    key_dict = json.load(f)
    db_hostname = key_dict['hostname']
    db_user = key_dict['user']
    db_passowrd = key_dict['password']
    db_database = key_dict['database']


#tenta a conexão
def connect():
    try:
        mydb = mysql.connector.connect(
        host=f"{db_hostname}",
        user=f"{db_user}",
        password=f"{db_passowrd}",
        database=f"{db_database}"
        )
    except:
        return None
    return mydb

#criação e inserção de dados no DB
class methods():
    #insere qualquer valor na tabela de usuário
    def insert_user(self, column, value, where, id):
        mydb = connect()
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
        mydb = connect()
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
        mydb = connect()
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
        mydb = connect()
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
    
    def insert_user(self, leads_id, user_id, search_date, keywords, leads_counter):
        mydb = connect()
        mycursor = mydb.cursor()
        try:
            sql = "INSERT INTO leads_generated (leadsid, userid, keywords, createdtimestamp, leads_counter) VALUES (%s, %s, %s, %s, %s)"
            val = (leads_id, user_id, ', '.join(keywords), search_date, leads_counter)
            mycursor.execute(sql, val)
        except mydb.Error as err:
            return None, err.errno
        finally:
            mydb.close()
        return mycursor.rowcount, "record inserted."

    
set = methods()

result, code = set.create_user("break2000123", "vinicius123", "vini@rafa", 2134566666)
business = set.create_business("Tecnosync.br1", 2, 2312421323)