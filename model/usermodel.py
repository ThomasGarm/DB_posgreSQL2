from .connection import Connection

class Usermodel:
    def __init__(self):
        self.db = Connection()
         #method for inserting message into the database
    def create_an_account(self, name, firstname, pseudo, email, age, password):
        self.db.initialize_connection()
        self.db.cursor.execute("INSERT INTO users (name, firstname, pseudo, email, age, password) VALUES (%s, %s, %s, %s, %s);",(name, firstname, pseudo, email, age, password))
        self.db.connection.commit()
        self.db.close_connection()
        


    def home_page(self):
        self.db.initialize_connection()
        self.db.cursor.execute("SELECT * FROM users;")
        messages = self.db.cursor.fetchall()
        self.db.close_connection()
        return messages

    def log_in(self, user, user_password):
        self.db.initialize_connection()
        self.db.cursor.execute("SELECT * FROM users WHERE pseudo=%s AND password=%s;"),(user, user_password)
