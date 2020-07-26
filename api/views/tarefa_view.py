from flask import make_response, request, jsonify
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from api import api
from ..entidades.tarefa import Tarefa
from ..models.tarefa_model import TarefaModel
from ..pagination import paginate
from ..schemas import tarefa_schema
from ..services import tarefa_service, projeto_service


class TarefaList(Resource):
    """metodos que não precisam de parametros GET e POST"""

    @jwt_required
    def get(self):
        """
        Lista de todas as tarefas
        ---
        parameters:
          - in: header
            name: Authorization
            type: string
            required: true
        responses:
          200:
            description: Lista de todas as tarefas
            schema:
              id: Tarefa
              properties:
                id:
                  type: integer
                titulo:
                  type: string
                descricao:
                  type: string
                data_expiracao:
                  type: string
                projeto:
                  type: string
          422:
            description: Token Inválido
        """
        # tarefas = tarefa_service.listar_tarefas()
        ts = tarefa_schema.TarefaSchema(many=True)
        # result = ts.jsonify(tarefas)
        # return make_response(result, 200)
        return paginate(TarefaModel, ts)

    def post(self):
        """
        Esta rota é responsável por cadastrar uma nova tarefa
        ---
        parameters:
          - in: body
            name: Tarefa
            description: Criar Nova Tarefa
            schema:
              type: object
              required:
                - titulo
                - descricao
                - data_expiracao
                - projeto
              properties:
                titulo:
                  type: string
                descricao:
                  type: string
                data_expiracao:
                  type: string
                projeto:
                  type: string
        responses:
          201:
            description: Tarefa Cadastrada com sucesso
            schema:
              id: Tarefa
              properties:
                titulo:
                  type: string
                descricao:
                  type: string
                data_expiracao:
                  type: string
                projeto:
                  type: string
          400:
            description: Tarefa não cadastrada - Dados inválidos
          404:
            description: Tarefa não cadastrada - Projeto não encontrado
        """
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
                return make_response(jsonify('Projeto não encontrado'), 404)
            tarefa_nova = Tarefa(titulo, descricao, data_expiracao, projeto)
            result = tarefa_service.cadastrar_tarefa(tarefa_nova)
            return make_response(ts.jsonify(result), 201)


class TarefaDetail(Resource):
    @jwt_required
    def get(self, id_tarefa):
        """
        Lista a tarefa que possui como Id o parâmetro
        ---
        parameters:
          - in: path
            name: id_tarefa
            type: integer
            required: true
          - in: header
            name: Authorization
            type: string
            required: true
        responses:
          200:
            description: Tarefa encontrada
            schema:
              id: Tarefa
              properties:
                id:
                  type: integer
                titulo:
                  type: string
                descricao:
                  type: string
                data_expiracao:
                  type: string
                projeto:
                  type: string
          422:
            description: Token Inválido
          404:
            description: Tarefa não encontrada
        """

        tarefa = tarefa_service.listar_tarefa_id(id_tarefa)
        if tarefa is None:
            return make_response(jsonify('Tarefa não encontrada'), 404)
        ts = tarefa_schema.TarefaSchema()
        return make_response(ts.jsonify(tarefa), 200)

    def put(self, id_tarefa):
        """
        Atualiza a tarefa que possui o id passado commo parâmetro
        ---
        parameters:
          - in: path
            name: id_tarefa
            type: integer
            requered: true
          - in: body
            name: Tarefa
            description: Atualizar tarefa por id
            schema:
              type: object
              required:
                - titulo
                - descricao
                - data_expiracao
                - projeto
              properties:
                titulo:
                  type: string
                descricao:
                  type: string
                data_expiracao:
                  type: string
                projeto:
                  type: string
        responses:
          200:
            description: Tarefa Atualizada com sucesso
            schema:
              id: Tarefa
              properties:
                titulo:
                  type: string
                descricao:
                  type: string
                data_expiracao:
                  type: string
                projeto:
                  type: string
          404:
            description: Tarefa não encontrada
          400:
            description: Tarefa não cadastrada - Dados inválidos
        """
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
        """
        Remove a tarefa que possui o Id igual o parâmetro id_tarefa
        ---
        parameters:
          - in: path
            name: id_tarefa
            type: integer
            required: true
        responses:
          204:
            description: Tarefa removida com sucesso
          404:
           description: Tarefa não encontrada
        """
        tarefa = tarefa_service.listar_tarefa_id(id_tarefa)

        if tarefa is None:
            return make_response(jsonify('Tarefa não encontrada'), 404)

        tarefa_service.deletar_tarefa(tarefa)
        return make_response('', 204)


api.add_resource(TarefaList, '/tarefas')
api.add_resource(TarefaDetail, '/tarefas/<int:id_tarefa>')
