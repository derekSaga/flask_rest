from api import db
from api.models import funcionario_model

funcionario_projeto = db.Table('funcionario_projeto',
                               db.Column('projeto_id', db.Integer, db.ForeignKey('projeto.id'), primary_key=True),
                               db.Column('funcionario_id', db.Integer, db.ForeignKey('funcionario.id'),
                                         primary_key=True)
                               )


class ProjetoModel(db.Model):
    __tablename__ = 'projeto'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(100), nullable=False)

    funcionarios = db.relationship(funcionario_model.FuncionarioModel, secondary="funcionario_projeto",
                                   back_populates="projetos")
