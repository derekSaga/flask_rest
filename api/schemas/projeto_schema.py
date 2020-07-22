from marshmallow import fields

from api import ma
from api.models.projeto_model import ProjetoModel


class ProjetoSchema(ma.SQLAlchemySchema):
    class Meta:
        model = ProjetoModel
        fields = ('id', 'nome', 'descricao', 'funcionarios', 'tarefas', '_links')
        ordered = True

    nome = fields.String(required=True)
    descricao = fields.String(required=True)
    funcionarios = ma.auto_field(required=True)
    tarefas = ma.auto_field()

    _links = ma.Hyperlinks(
        {
            "get": ma.URLFor("projetodetail", id_projeto="<id>"),
            "put": ma.URLFor('projetodetail', id_projeto="<id>"),
            "delete": ma.URLFor("projetodetail", id_projeto="<id>")
        }
    )
