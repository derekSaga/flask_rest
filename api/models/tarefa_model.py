from api import db
from api.models import projeto_model


class TarefaModel(db.Model):
    __tablename__ = 'tarefa'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(100), nullable=False)
    data_expiracao = db.Column(db.DATE, nullable=False)

    projeto_id = db.Column(db.Integer, db.ForeignKey('projeto.id'))

    projeto = db.relationship(projeto_model.ProjetoModel, backref=db.backref('tarefas', lazy='dynamic'))
