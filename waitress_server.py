from main import app
from flask_migrate import Migrate
from data import db_session
from flask_restful import Api
from api import record_resources
import os


if __name__ == '__main__':
    db = db_session.global_init("postgres://edfgqwwnxaatqk:21da450b0900c800d3db53aa7e48060cb58227e10a07d449e592"
                                "9ef9f4819b7b@ec2-52-1-115-6.compute-1.amazonaws.com:5432/djjunfccgq5gk")
    migrate = Migrate(app, db)
    api = Api(app)
    # для списка объектов
    api.add_resource(record_resources.RecordListResource, '/api/records')

    # для одного объекта
    api.add_resource(record_resources.RecordResource, '/api/record/<int:record_id>')
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)