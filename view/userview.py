from model.usermodel import Usermodel

class Userview():
    def __init__(self):
        self.usermodel = Usermodel()

    def to_log_in(self, pseudo):
        pseudo = input("Entrez votre pseudo  ")
        self.usermodel.log_in(pseudo)

    def new_account(self):
        name = input("Entrez votre nom")
        firstname = input("Entrez votre prénom")
        pseudo = input("Entrez votre pseudo")
        email = input("Entrez votre mail")
        age = input("Entrez votre age")
        password = input("Entrez votre password")
        self.usermodel.create_an_account(name, firstname, pseudo, email, age, password)