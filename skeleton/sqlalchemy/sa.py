# -*-coding:utf-8-*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects import mysql
from sqlalchemy import Column, String, Float, Integer
from sqlalchemy.dialects.mysql import INTEGER


def to_dict(self):
    return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}


Base = declarative_base()
Base.to_dict = to_dict


mysql_dialect_object = mysql.dialect()


def query_to_sql(query, dialect=mysql_dialect_object):
    sql = query.statement.compile(dialect=dialect, compile_kwargs={"literal_binds": True})
    return str(sql)


class Music(Base):

    __tablename__ = 'music'

    song_id = Column(String(64), primary_key=True)
    song_name = Column(String(256), nullable=True)
    artist_rank = Column(INTEGER(20))


# create_engine

from sqlalchemy import create_engine
# pip install mysql-connector-python
url = 'mysql+mysqlconnector://{}:{}@{}/{}?charset=utf8'.format(user, passwd, host, db)
engine = create_engine(url)

# session
from sqlalchemy.orm import scoped_session, sessionmaker
session = sessionmaker(bind=engine)

# query
session.query(Music).filter_by(song_name='what is love?')


# -------------- Column说明 ----------------------

FLOAT(10, 2)  # 8位整数，2位小数