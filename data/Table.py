import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase

class Cat(SqlAlchemyBase):
    __tablename__ = 'cats'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    color = sqlalchemy.Column(sqlalchemy.String, nullable=False) #Я так понял что порода - это цвет
    age = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    description = sqlalchemy.Column(sqlalchemy.String)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                     default=datetime.datetime.now)

    def __repr__(self):
        return f"{self.id},{self.color},{self.age},{self.description}"