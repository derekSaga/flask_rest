class Tarefa:
    def __init__(self, titulo, descricao, data_expiracao, projeto_id):
        self.__titulo = titulo
        self.__data_expiracao = data_expiracao
        self.__descricao = descricao
        self.__projeto_id = projeto_id

    @property
    def projeto_id(self):
        return self.__projeto_id

    @projeto_id.setter
    def projeto_id(self, projeto):
        self.__projeto_id = projeto

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def data_expiracao(self):
        return self.__data_expiracao

    @data_expiracao.setter
    def data_expiracao(self, data_expiracao):
        self.__data_expiracao = data_expiracao

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao
