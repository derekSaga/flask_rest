from datetime import timedelta

from flask import request, make_response, jsonify
from flask_jwt_extended import create_access_token
from flask_restful import Resource

from api import api
from api.models import usuario_model
from api.schemas.login_schema import LoginSchema
from api.schemas.usuario_schema import UsuarioSchema
from api.services import usuario_service


class LoginList(Resource):
    def post(self):
        us = LoginSchema()
        validate = us.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            email = request.json['email']
            senha = request.json['senha']
            usuario_bd = usuario_service.listar_usuario(email)
            val = usuario_bd and usuario_bd.ver_senha(senha)
            if val:
                access_token = create_access_token(identity=usuario_bd.id,
                                                   expires_delta=timedelta(seconds=60))
                return make_response(jsonify(
                    {'access_token': access_token,
                     'message': 'login realizado com sucesso'}
                ), 200)
            else:
                return make_response(jsonify({'message': 'login realizado com sucesso'}),
                                     401)


api.add_resource(LoginList, '/login')
