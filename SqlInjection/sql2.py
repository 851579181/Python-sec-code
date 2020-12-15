# -*- coding：utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def yds(name):
    db_conn = 'mysql+pymysql://{username}:{password}@{ip}/{database}?charset=utf8'.format("root","wxf","localhost","test")
    engine = create_engine(db_conn)
    session = sessionmaker(bind=engine())()
    sql = 'select * from users where name="%s"' % name
    objs = session.execute(sql)

