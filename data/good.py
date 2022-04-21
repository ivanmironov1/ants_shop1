import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Good(SqlAlchemyBase):
    __tablename__ = "good"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    price = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)

    customer_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"), nullable=True)
    customer = orm.relation('User')

    image_name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    description = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    type = sqlalchemy.Column(sqlalchemy.String, nullable=True)


class GoodMethods:
    def __init__(self, db_session):
        self.db_session = db_session

    def get_all_goods(self, type_):
        session = self.db_session.create_session()
        goods = session.query(Good).filter(Good.type == type_, Good.customer_id == sqlalchemy.sql.null())
        return goods

    def get(self, id_):
        session = self.db_session.create_session()
        return session.query(Good).get(id_)

    def set_customer(self, good_id, user_id):
        session = self.db_session.create_session()
        good = session.query(Good).get(good_id)
        good.customer_id = user_id
        session.commit()