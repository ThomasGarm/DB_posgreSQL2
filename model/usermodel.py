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
        


    """def home_page(self):
        self.db.initialize_connection()
        self.db.cursor.execute("SELECT * FROM users;")
        messages = self.db.cursor.fetchall()
        self.db.close_connection()
        return messages"""

    def log_in(self, pseudo):
        self.db.initialize_connection()
        self.db.cursor.execute("SELECT * FROM users WHERE pseudo=%s);",(pseudo))
        user_raw =  self.db.cursor.fetchone()
        self.db.close_connection()
        return user_raw

    def delete_account(self, pseudo):
        self.db.initialize_connection()
        self.db.cursor.execute("DELETE FROM users WHERE pseudo = %s);"(pseudo))
        self.db.connection.commit()
        self.db.close_connection()

    def update_an_account(self, column, value, pseudo):
        self.db.initialize_connection()
        self.db.cursor.execute("UPDATE FROM users set %s = %s WHERE pseudo = %s);"(column, value, pseudo))
        self.db.connection.commit()
        self.db.close_connection()



