from flask import make_response, request, jsonify
from flask_restful import Resource

from api import api
from api.entidades.tarefa import Tarefa
from api.models.tarefa_model import TarefaModel
from api.pagination import paginate
from api.schemas import tarefa_schema
from api.services import tarefa_service, projeto_service


class TarefaList(Resource):
    """metodos que não precisam de parametros GET e POST"""

    def get(self):
        # tarefas = tarefa_service.listar_tarefas()
        ts = tarefa_schema.TarefaSchema(many=True)
        # result = ts.jsonify(tarefas)
        # return make_response(result, 200)
        return paginate(TarefaModel, ts)

    def post(self):
        ts = tarefa_schema.TarefaSchema()
        validate = ts.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            titulo = request.json['titulo']
            descricao = request.json['descricao']
            data_expiracao = request.json['data_expiracao']
            projeto = request.json['projeto']
            projeto_tarefa = projeto_service.listar_projeto_id(projeto)
            if projeto_tarefa is None:
                return make_response(jsonify('Projeto não encontrada'), 404)
            tarefa_nova = Tarefa(titulo, descricao, data_expiracao, projeto)
            result = tarefa_service.cadastrar_tarefa(tarefa_nova)
            return make_response(ts.jsonify(result), 201)


class TarefaDetail(Resource):

    def get(self, id_tarefa):
        tarefa = tarefa_service.listar_tarefa_id(id_tarefa)
        if tarefa is None:
            return make_response(jsonify('Tarefa não encontrada'), 404)
        ts = tarefa_schema.TarefaSchema()
        return make_response(ts.jsonify(tarefa), 200)

    def put(self, id_tarefa):

        tarefa_bd = tarefa_service.listar_tarefa_id(id_tarefa)

        if tarefa_bd is None:
            return make_response(jsonify('Tarefa não encontrada'), 404)
        ts = tarefa_schema.TarefaSchema()

        validate = ts.validate(request.json)

        if validate:
            return make_response(ts.jsonify(validate), 400)
        else:
            titulo = request.json['titulo']
            descricao = request.json['descricao']
            data_expiracao = request.json['data_expiracao']
            projeto = request.json['projeto']

            tarefa_nova = Tarefa(titulo, descricao, data_expiracao, projeto)

            tarefa_service.editar_tarefa(tarefa_bd, tarefa_nova)

            tarefa_atualizada = tarefa_service.listar_tarefa_id(id_tarefa)

            return make_response(ts.jsonify(tarefa_atualizada), 200)

    def delete(self, id_tarefa):
        tarefa = tarefa_service.listar_tarefa_id(id_tarefa)

        if tarefa is None:
            return make_response(jsonify('Tarefa não encontrada'), 404)

        tarefa_service.deletar_tarefa(tarefa)
        return make_response('', 204)


api.add_resource(TarefaList, '/tarefas')
api.add_resource(TarefaDetail, '/tarefas/<int:id_tarefa>')
