import datetime
import sqlalchemy
from app import db
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin


class Complaint(db.Model, SerializerMixin):
    __tablename__ = 'complaints'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    author = sqlalchemy.Column(sqlalchemy.Integer,
                                    sqlalchemy.ForeignKey("users.id"))
    date_create = sqlalchemy.Column(sqlalchemy.DateTime,
                                   default=datetime.datetime.now)
    comment_id = sqlalchemy.Column(sqlalchemy.Integer,
                                    sqlalchemy.ForeignKey("comments.id"))
    user = orm.relation('User')
    comment = orm.relation("Comment")