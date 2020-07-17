class Funcionario:

    def __init__(self, nome, dt_nascimento):
        self._nome = nome
        self._dt_nascimento = dt_nascimento

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def dt_nascimento(self):
        return self._dt_nascimento

    @dt_nascimento.setter
    def dt_nascimento(self, dt_nascimento):
        self._dt_nascimento = dt_nascimento
