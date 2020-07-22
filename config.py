import uuid

DEBUG = True
USERNAME = 'root'
PASSWORD = '7P952wjy*'
SERVER = 'localhost'
DB = 'flask_api'

SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}?charset=utf8mb4'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = str(uuid.uuid4())
JSON_SORT_KEYS = False
