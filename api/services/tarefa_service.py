from api import db
from api.models.tarefa_model import TarefaModel


def cadastrar_tarefa(tarefa):
    tarefa_bd = TarefaModel(titulo=tarefa.titulo,
                            descricao=tarefa.descricao,
                            data_expiracao=tarefa.data_expiracao,
                            projeto_id=tarefa.projeto_id)
    session = db.session

    try:
        session.add(tarefa_bd)
        session.commit()
        return tarefa_bd
    except Exception as e:
        session.rollback()
        raise e


def listar_tarefas():
    try:
        tarefas = TarefaModel.query.all()
        return tarefas
    except Exception as e:
        raise e


def listar_tarefa_id(id: int) -> TarefaModel:
    try:
        tarefa = TarefaModel.query.filter(TarefaModel.id == id).first()
        return tarefa
    except Exception as e:
        raise e


def editar_tarefa(tarefa_bd, tarefa_nova):
    try:
        tarefa_bd.titulo = tarefa_nova.titulo
        tarefa_bd.descricao = tarefa_nova.descricao
        tarefa_bd.data_expiracao = tarefa_nova.data_expiracao
        tarefa_bd.projeto_id = tarefa_nova.projeto_id
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e


def deletar_tarefa(tarefa):
    try:
        db.session.delete(tarefa)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e
