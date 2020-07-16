from api import db
from api.models.projeto_model import ProjetoModel


def cadastrar_projeto(projeto):
    projeto_bd = ProjetoModel(nome=projeto.nome,
                              descricao=projeto.descricao)
    session = db.session
    try:
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
        raise e


def listar_projeto_id(id: int) -> ProjetoModel:
    try:
        projeto = ProjetoModel.query.filter(ProjetoModel.id == id).first()
        return projeto
    except Exception as e:
        raise e


def editar_projeto(projeto_bd, projeto_nova):
    try:
        projeto_bd.nome = projeto_nova.nome
        projeto_bd.descricao = projeto_nova.descricao
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
