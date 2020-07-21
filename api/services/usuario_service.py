from api import db
from api.models import usuario_model


def cadastrar_usuario(usuario):
    usuario_db = usuario_model.UsuarioModel(nome=usuario.nome,
                                            email=usuario.email,
                                            senha=usuario.senha)

    usuario_db.gen_senha()
    try:
        db.session.add(usuario_db)
        db.session.commit()
        return usuario_db
    except Exception as e:
        db.session.rollback()
        raise e


def listar_usuario(email):
    return usuario_model.UsuarioModel.query.filter(usuario_model.UsuarioModel.email == email).first()
