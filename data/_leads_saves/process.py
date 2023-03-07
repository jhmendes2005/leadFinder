from _db_process import connector


class leads():

    def __init__(self, lead_id, user_id, search_date, keywords) -> None:
        self.leads_id = lead_id
        self.user_id = user_id
        self.search_date = search_date
        self.keywords = keywords

        return "Leads salvos em memória para serem processados."


    def insert_user(self):
        mydb = connector.connect()
        mycursor = mydb.cursor()
        try:
            sql = "INSERT INTO leads_generated (leadsid, userid, keywords, createdtimestamp) VALUES (%s, %s, %s, %s)"
            val = (self.leads_id, self.user_id, ', '.join(self.keywords), self.search_date)
            mycursor.execute(sql, val)
        except mydb.Error as err:
            return None, err.errno
        finally:
            mydb.close()
        return mycursor.rowcount, "record inserted."