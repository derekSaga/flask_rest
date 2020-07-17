from marshmallow import fields

from api import ma
from api.models import funcionario_model


class FuncionarioSchema(ma.Schema):
    class Meta:
        model = funcionario_model.FuncionarioModel
        fields = ("nome", "dt_nascimento")

    nome = fields.String(required=True)
    dt_nascimento = fields.Date(required=True)
