import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin


class Сomplaint(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'complaints'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    author = sqlalchemy.Column(sqlalchemy.Integer,
                                    sqlalchemy.ForeignKey("users.id"))
    reason = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    date_create = sqlalchemy.Column(sqlalchemy.DateTime,
                                   default=datetime.datetime.now)
    comment_id = sqlalchemy.Column(sqlalchemy.Integer,
                                    sqlalchemy.ForeignKey("comments.id"))
    user = orm.relation('User')
    comments = orm.relation("Comment")