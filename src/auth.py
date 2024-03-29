import pyodbc

conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=PC\SQLEXPRESS;"
    "DATABASE=Crypto;"
    "Trusted_Connection=yes;"
)
cursor = conn.cursor()

class User:
    def __init__(self):
        self.override = False

    def login(self, username, password):
        if self.override == False:
            q = "SELECT * FROM users WHERE username = ? AND password = ?"
            r = cursor.execute(q, (username, password))
            return r.rowcount

             
    def register(self,username,password):
        if self.override == False:
            q = "INSERT INTO users (username,password) VALUES (?,?)"
            r = cursor.execute(q, (username,password))
            conn.commit()
            return r.rowcount
        
u = User()
