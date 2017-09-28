#!/usr/bin/env python
#-*- coding:utf-8 -*-
import pymysql
# connect to the database
connection = pymysql.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '',
    db = 'py_explore',
    charset = 'utf8'
)

# operate the database
try:
    with connection.cursor() as cursor:
        sql = 'insert into `users` (`email`, `password`) values (%s, %s)'
        cursor.execute(sql, ('2json@weidian.com', '123456'))
    # 数据库默认不会自动提交保存的，需要我们手动的commit
    connection.commit()

    # 执行一个查询操作
    with connection.cursor() as cursor:
        sql = 'select * from `users` where `email` = %s'
        cursor.execute(sql, ('2json@weidian.com',))
        result = cursor.fetchone()
        print result
finally:
    connection.close()