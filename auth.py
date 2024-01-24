import pyodbc

conn = pyodbc.connect('DRIVER= {ODBC Driver 17 for SQL Server}; \
                        SERVER=cryptoappdb.cxo46i8keynk.us-west-1.rds.amazonaws.com; \
                        DATABASE=users; \
                        UID=admin;\
                        PWD=admin1234')
cursor = conn.cursor()

class User:
    def __init__(self):
        self.override = False

    def login(self, username, password):
        if self.override == False:
            q = "SELECT * FROM main WHERE users = ? AND password = ?"
            r = cursor.execute(q, (username, password))
            return bool(r)

             
    def register(self,username,password):
        if self.override == False:
            q = f"INSERT INTO main (users,password) VALUES ?, ?)"
            r = cursor.execute(q,(username,password))
            return bool(r)
