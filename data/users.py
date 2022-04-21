import datetime
import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = "users"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    chat_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    balance = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    referrer = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    amount_purchases = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    ref_earnings = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)

    purchases = orm.relation("Good", back_populates='customer')


class UserMethods:
    def __init__(self, db_session):
        self.db_session = db_session

    def get_all_chat_ids(self):
        session = self.db_session.create_session()
        chat_ids = session.query(User.chat_id).all()
        chat_ids = [i[0] for i in chat_ids]
        return chat_ids

    def add(self, chat_id, referrer):
        session = self.db_session.create_session()
        user = User(
            chat_id=chat_id,
            referrer=referrer,
            balance=0,
            amount_purchases=0
        )
        session.add(user)
        session.commit()

    def get(self, id_):
        session = self.db_session.create_session()
        return session.query(User).filter(User.chat_id == id_).first()

    def new_purchase(self, id_, delta):
        session = self.db_session.create_session()
        user = session.query(User).filter(User.chat_id == id_).first()
        user.balance -= delta
        user.amount_purchases += delta
        session.commit()

    def add_balance(self, id_, delta):
        session = self.db_session.create_session()
        user = session.query(User).filter(User.chat_id == id_).first()
        user.balance += delta
        session.commit()
