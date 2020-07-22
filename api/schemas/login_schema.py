from marshmallow import fields

from api import ma
from api.models import usuario_model


class LoginSchema(ma.SQLAlchemySchema):
    class Meta:
        model = usuario_model.UsuarioModel

    senha = fields.String(required=True)
    email = fields.String(required=True)
