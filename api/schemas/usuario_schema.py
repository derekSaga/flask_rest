from marshmallow import fields

from api import ma
from api.models import usuario_model


class UsuarioSchema(ma.SQLAlchemySchema):
    class:
        model = usuario_model.UsuarioModel
        fields = ('id', 'nome', 'senha', 'email')

    nome = fields.String(required=True)
    senha = fields.String(required=True)
    email = fields.String(required=True)
