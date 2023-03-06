import mysql.connector
import json

#obtém as informações do DB
with open('./data/_db_process/host.json', 'r') as f:
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

#fecha a conexão
def close_connect(db):
    db.close()
    return True

""" Códigos de erro:
except self.mydb.connector.Error as err:
print(err)
print("Error Code:", err.errno)
print("SQLSTATE", err.sqlstate)
print("Message", err.msg) """