class Usuario:
    def __init__(self, nome=None, senha=None, email=None):
        self.__nome = nome
        self.__senha = senha
        self.__email = email

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha):
        self.__senha = senha

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email
