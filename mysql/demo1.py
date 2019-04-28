import pymysql

db = pymysql.connect(host='192.168.11.138', user='root', password='654321', port=3306, db='spiders')
cursor = db.cursor()
# cursor.execute('SELECT VERSION()')
# data = cursor.fetchone()
# print('Database version', data)
# cursor.execute("create database spiders default character set utf8")
# db.close()

# sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))'
# cursor.execute(sql)
# db.close()

# id = '20182101'
# user = 'Bob'
# age = 23
#
# sql = 'INSERT INTO students(id, name, age) values(%s, %s, %s)'
# try:
#     cursor.execute(sql, (id, user, age))
#     db.commit()
# except:
#     db.rollback()
#
# db.close()


data = {
    'id': '20120001',
    'name': 'Bob',
    'age': 20
}

# table = 'students'
# keys = ', '.join(data.keys())
# values = ', '.join(['%s'] * len(data))
# sql = 'insert into {table} ({keys}) values ({values})'.format(table=table, keys=keys, values=values)
# try:
#     cursor.execute(sql, tuple(data.values()))
#     db.commit()
# except:
#     db.rollback()
#
# db.close()

sql = 'select * from students where age >= 25'
try:
    cursor.execute(sql)
    print('Count:', cursor.rowcount)
    row = cursor.fetchone()
    while row:
        print('Row:', row)
        row = cursor.fetchone()
except:
    print('Error')