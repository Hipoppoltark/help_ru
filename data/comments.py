import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin


class Comment(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'comments'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    author = sqlalchemy.Column(sqlalchemy.Integer,
                               sqlalchemy.ForeignKey("users.id"))
    comment = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    record_id = sqlalchemy.Column(sqlalchemy.Integer,
                               sqlalchemy.ForeignKey("records.id"))
    estimation = sqlalchemy.Column(sqlalchemy.Float, nullable=True, default=0.0)
    date_create = sqlalchemy.Column(sqlalchemy.DateTime,
                                    default=datetime.datetime.now)
    # users_who_gave_rating =
    user = orm.relation('User')
    record = orm.relation('Record')
    ratings = orm.relation('Rating', back_populates='comment')