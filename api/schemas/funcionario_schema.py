from marshmallow import fields

from api import ma
from ..models import funcionario_model


class FuncionarioSchema(ma.SQLAlchemySchema):
    class Meta:
        model = funcionario_model.FuncionarioModel
        fields = ("id", "nome", "dt_nascimento", "projetos", '_links')
        ordered = True

    nome = fields.String(required=True)
    dt_nascimento = fields.Date(required=True)
    projetos = ma.auto_field()

    _links = ma.Hyperlinks(
        {
            "get": ma.URLFor("funcionariodetail", id_funcionario="<id>"),
            "put": ma.URLFor('funcionariodetail', id_funcionario="<id>"),
            "delete": ma.URLFor("funcionariodetail", id_funcionario="<id>")
        }
    )
