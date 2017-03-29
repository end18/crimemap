import pymysql
import dbconfig
connection = pymysql.connect(host='localhost', 
                             user=dbconfig.db_user, 
                             passwd=dbconfig.db_passwd)
try:
    with connection.cursor() as cursor:
        sql = "Create database if not exists crimemap"
        cursor.execute(sql)
        sql = """ Create table if not exists 
        crimemap.crimes(
        id int not null auto_increment,
        latitude float(10,6),
        longitude float(10,6),
        date datetime,
        categotry varchar(50),
        description varchar(1000),
        update_at timestamp,
        primary key(id)
        )"""
        cursor.execute(sql)
        connection.commit()
finally:
    connection.close()
