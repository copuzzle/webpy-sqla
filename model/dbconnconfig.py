# -*- coding:utf-8 -*-
from sqlalchemy import create_engine

#数据库连接字符串
DB_CONNECT_STRING = "mysql+mysqldb://root:pass@192.168.1.1/testdb?charset=utf8"
engine = create_engine(DB_CONNECT_STRING, echo=True)

if __name__ == "__main__":
    conn = engine.connect()
    # this is a connecting test
    tables = conn.execute("show tables;")
    record = conn.execute("select * from Letsgo_UsersCode")
    print tables.fetchall()
    print record.fetchall()


