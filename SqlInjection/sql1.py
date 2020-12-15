# -*- coding：utf-8 -*-
import pymysql

def yds(name):
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="wxf",db="test")
    cursor = conn.cursor()
    cursor.execute("select * from users where name = \"%s\"" % name)
