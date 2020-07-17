from api import db


class FuncionarioModel(db.Model):

    __tablename__ = 'funcionario'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(80), nullable=False)
    dt_nascimento = db.Column(db.DATE, nullable=False)

    