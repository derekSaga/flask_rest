from marshmallow import fields

from api import ma
from ..models import funcionario_model


class FuncionarioSchema(ma.SQLAlchemySchema):
    class Meta:
        model = funcionario_model.FuncionarioModel
        fields = ("id", "nome", "dt_nascimento", "projetos")

    nome = fields.String(required=True)
    dt_nascimento = fields.Date(required=True)
    projetos = ma.auto_field()
