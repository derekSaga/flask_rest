from api import db


class ProjetoModel(db.Model):
    __tablename__ = 'projeto'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(100), nullable=False)
