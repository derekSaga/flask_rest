from flask import make_response, request, jsonify
from flask_restful import Resource

from api import api
from api.entidades import funcionario
from api.schemas import funcionario_schema
from api.services import funcionario_service


class FuncionarioList(Resource):
    """metodos get e post que não precisam de parametros"""

    def get(self):
        funcionarios = funcionario_service.listar_funcionarios()
        fs = funcionario_schema.FuncionarioSchema(many=True)
        result = fs.jsonify(funcionarios)
        return make_response(result, 200)

    def post(self):
        fs = funcionario_schema.FuncionarioSchema()
        validate = fs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json['nome']
            dt_nascimento = request.json['dt_nascimento']
            funcionario_entidade = funcionario.Funcionario(nome, dt_nascimento)
            result = funcionario_service.cadastrar_funcionario(funcionario_entidade)
            return make_response(fs.jsonify(result), 201)


class FuncionarioDetail(Resource):
    def get(self, id_funcionario):
        funcionario_bd = funcionario_service.listar_funcionario_id(id_funcionario)
        if funcionario_bd is None:
            return make_response(jsonify('Funcionario não encontrado'), 404)
        fs = funcionario_schema.FuncionarioSchema()
        return make_response(fs.jsonify(funcionario_bd), 200)

    def delete(self, id_funcionario):
        funcionario_bd = funcionario_service.listar_funcionario_id(id_funcionario)
        if funcionario_bd is None:
            return make_response(jsonify('Funcionario não encontrado'), 404)
        funcionario_service.delete_funcionario(funcionario_bd)
        return make_response(jsonify(''), 204)


api.add_resource(FuncionarioList, '/funcionarios')
api.add_resource(FuncionarioDetail, '/funcionarios/<int:id_funcionario>')
