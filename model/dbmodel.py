# -*- coding: utf-8 -*-
from dbconnconfig import engine
#from sqlalchemy.orm import deferred, mapper, defer
#from sqlalchemy import Table, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.dialects.mysql import \
        BIGINT, BINARY, BIT, BLOB, BOOLEAN, CHAR, DATE, \
        DATETIME, DECIMAL, DECIMAL, DOUBLE, ENUM, FLOAT, INTEGER, \
        LONGBLOB, LONGTEXT, MEDIUMBLOB, MEDIUMINT, MEDIUMTEXT, NCHAR, \
        NUMERIC, NVARCHAR, REAL, SET, SMALLINT, TEXT, TIME, TIMESTAMP, \
        TINYBLOB, TINYINT, TINYTEXT, VARBINARY, VARCHAR, YEAR
from sqlalchemy import Integer, String, Text, Binary, Column

Base = declarative_base()


#基本设置
class Setting(Base):
    __tablename__ = "Letsgo_Setting"
    id = Column(Integer, primary_key=True, nullable=False)
    task2_money = Column(DECIMAL(10, 2), nullable=False)
    task3_money = Column(DECIMAL(10, 2), nullable=False)
    task3_1_money = Column(DECIMAL(10, 2), nullable=False)
    code_perday = Column(String(255), nullable=False)
    def __repr__(self):
        return self.__class__.__name__


def init_repositoey():
    Session = scoped_session(sessionmaker(bind=engine))
    Base.metadata.create_all(engine)
    session = Session()
    return session.query(OrderInfo)


def myinsert():
    Session = scoped_session(sessionmaker(bind=engine))
    Base.metadata.create_all(engine)
    session = Session()

    usercode = UserCode()
    usercode.userid_owner = 32143343434
    usercode.code_num = 'this is a test recode'
    usercode.userid_user = 999
    usercode.create_time = 20121212
    usercode.use_time = 20131203
    session.add(usercode)
    return session.commit()


if __name__ == "__main__":
    Session = scoped_session(sessionmaker(bind=engine))

    #qq= init_repositoey()
    #print qq.first()
    #print myinsert()
    print 'XXX'
    session = Session()
    phone_record =Session.query(Users).filter(Users.user_name == '324').first()
    user_code = Session.query(UserCode).first()
    print phone_record
    print user_code.__dict__
