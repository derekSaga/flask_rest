from api import db
from api.models.funcionario_model import FuncionarioModel


def cadastrar_funcionario(funcionario):
    funcionario_db = FuncionarioModel(nome=funcionario.nome, dt_nascimento=funcionario.dt_nascimento)
    session = db.session
    try:
        session.add(funcionario_db)
        session.commit()
        return funcionario_db
    except Exception as e:
        session.rollback()
        raise e


def listar_funcionario_id(id_funcionario):
    try:
        funcionario = FuncionarioModel.query.filter(FuncionarioModel.id == id_funcionario).first()
        return funcionario
    except Exception as e:
        raise e


def listar_funcionarios():
    try:
        funcionarios = FuncionarioModel.query.all()
        return funcionarios
    except Exception as e:
        raise e


def delete_funcionario(funcionario_db):
    session = db.session
    try:
        session.delete(funcionario_db)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e


def editar_funcionario(funcionario_db, funcionario):
    session = db.session
    try:
        funcionario_db.nome = funcionario.nome
        funcionario_db.dt_nascimento = funcionario.dt_nascimento
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
