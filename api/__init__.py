from flask import Flask
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)
api = Api(app)
JWTManager(app)

from .views import tarefa_view, projeto_view, funcionario_view, usuario_view, login_views
from .models import tarefa_model, projeto_model, funcionario_model, usuario_model
