from flask import request, make_response, jsonify
from flask_restful import Resource

from api import api
from api.entidades.projeto import Projeto
from api.schemas import projeto_schema
from api.services import projeto_service


class ProjetoList(Resource):
    """metodos que não precisam de parametros GET e POST"""

    def get(self):
        projetos = projeto_service.listar_projetos()
        ts = projeto_schema.ProjetoSchema(many=True)
        result = ts.jsonify(projetos)
        return make_response(result, 200)

    def post(self):
        ts = projeto_schema.ProjetoSchema()
        validate = ts.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json['nome']
            descricao = request.json['descricao']
            projeto_nova = Projeto(nome, descricao)
            result = projeto_service.cadastrar_projeto(projeto_nova)
            return make_response(ts.jsonify(result), 201)


class ProjetoDetail(Resource):

    def get(self, id_projeto):
        projeto = projeto_service.listar_projeto_id(id_projeto)
        if projeto is None:
            return make_response(jsonify('Projeto não encontrada'), 404)
        ts = projeto_schema.ProjetoSchema()
        return make_response(ts.jsonify(projeto), 200)

    def put(self, id_projeto):

        projeto_bd = projeto_service.listar_projeto_id(id_projeto)

        if projeto_bd is None:
            return make_response(jsonify('Projeto não encontrada'), 404)
        ts = projeto_schema.ProjetoSchema()

        validate = ts.validate(request.json)

        if validate:
            return make_response(ts.jsonify(validate), 400)
        else:
            nome = request.json['nome']
            descricao = request.json['descricao']

            projeto_nova = Projeto(nome, descricao)

            projeto_service.editar_projeto(projeto_bd, projeto_nova)

            projeto_atualizada = projeto_service.listar_projeto_id(id_projeto)

            return make_response(ts.jsonify(projeto_atualizada), 200)

    def delete(self, id_projeto):
        projeto = projeto_service.listar_projeto_id(id_projeto)

        if projeto is None:
            return make_response(jsonify('Projeto não encontrada'), 404)

        projeto_service.deletar_projeto(projeto)
        return make_response('', 204)


api.add_resource(ProjetoList, '/projetos')
api.add_resource(ProjetoDetail, '/projetos/<int:id_projeto>')
