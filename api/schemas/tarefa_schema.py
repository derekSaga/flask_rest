from marshmallow import fields

from api import ma
from ..models import tarefa_model


class TarefaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = tarefa_model.TarefaModel
        fields = ("id", "titulo", "descricao", "data_expiracao", "projeto", "_links")
        ordered = True

    titulo = fields.String(required=True)
    descricao = fields.String(required=True)
    data_expiracao = fields.Date(required=True)
    projeto = ma.auto_field(required=True)

    _links = ma.Hyperlinks(
        {
            "get": ma.URLFor("tarefadetail", id_tarefa="<id>"),
            "put": ma.URLFor('tarefadetail', id_tarefa="<id>"),
            "delete": ma.URLFor("tarefadetail", id_tarefa="<id>")
        }
    )
