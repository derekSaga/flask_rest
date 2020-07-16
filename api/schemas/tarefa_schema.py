from marshmallow import fields

from api import ma
from api.models.tarefa_model import TarefaModel


class TarefaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = TarefaModel
        fields = ('titulo', 'descricao', 'data_expiracao', 'projeto')

    titulo = fields.String(required=True)
    descricao = fields.String(required=True)
    data_expiracao = fields.Date(required=True)
    projeto = fields.String(required=True)
