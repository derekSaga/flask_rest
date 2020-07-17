from marshmallow import fields

from api import ma
from api.models import projeto_model


class ProjetoSchema(ma.Schema):
    class Meta:
        model = projeto_model.ProjetoModel
        fields = ("id", "nome", "descricao", "tarefas")
        ordered = True

    nome = fields.String(required=True)
    descricao = fields.String(required=True)
    tarefas = fields.List(fields.String)
