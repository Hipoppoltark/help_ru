from flask import Flask, request, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_restful import Api
from api import record_resources

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres+psycopg2://edfgqwwnxaatqk:21da450b0900c800d3db53aa7e48060cb58227e' \
                                            '10a07d449e5929ef9f4819b7b@ec2-52-1-115-6.compute-1.amazonaws.com:5432/djj' \
                                            'unfccgq5gk'
    api = Api(app)
    # для списка объектов
    api.add_resource(record_resources.RecordListResource, '/api/records')

    # для одного объекта
    api.add_resource(record_resources.RecordResource, '/api/record/<int:record_id>')
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    return app


from data import __all_models