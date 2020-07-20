from api import db
from api.models.projeto_model import ProjetoModel
from api.services import funcionario_service


def cadastrar_projeto(projeto):
    projeto_bd = ProjetoModel(nome=projeto.nome,
                              descricao=projeto.descricao)
    session = db.session
    try:
        for id_func in projeto.funcionarios:
            func_db = funcionario_service.listar_funcionario_id(id_func)
            projeto_bd.funcionarios.append(func_db)

        session.add(projeto_bd)
        session.commit()
        return projeto_bd
    except Exception as e:
        session.rollback()
        raise e


def listar_projetos():
    try:
        projetos = ProjetoModel.query.all()
        return projetos
    except Exception as e:
        print(e)
        raise e


def listar_projeto_id(id):
    try:
        projeto = ProjetoModel.query.filter(ProjetoModel.id == id).first()
        return projeto
    except Exception as e:
        raise e


def editar_projeto(projeto_bd, projeto_nova):
    try:
        projeto_bd.nome = projeto_nova.nome
        projeto_bd.descricao = projeto_nova.descricao
        projeto_bd.funcionarios = list()
        for i in projeto_nova.funcionarios:
            func = funcionario_service.listar_funcionario_id(i)
            projeto_bd.funcionarios.append(func)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e


def deletar_projeto(projeto):
    try:
        db.session.delete(projeto)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e
