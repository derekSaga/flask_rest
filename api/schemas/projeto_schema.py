from marshmallow import fields

from api import ma
from api.models.projeto_model import ProjetoModel


class ProjetoSchema(ma.SQLAlchemySchema):
    class Meta:
        model = ProjetoModel
        fields = ('id', 'nome', 'funcionarios', 'tarefas', 'descricao')

    nome = fields.String(required=True)
    descricao = fields.String(required=True)
    funcionarios = ma.auto_field(required=True)
    tarefas = ma.auto_field()
