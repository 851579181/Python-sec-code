# -*- coding：utf-8 -*-
import MySQLdb

def yds(name):
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='wxf',
        db='test',
    )
    cur = conn.cursor()
    sql = "select * from users where name=\"%s\"" % name
    cur.execute(sql)
