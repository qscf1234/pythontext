import pymysql

db = pymysql.connect("localhost", "root", "root", "kaige")
cursor = db.cursor()

# 检查表是否存在，如果存在删除
cursor.execute('drop table if exists bandcard')

sql = 'create table bandcard(id int auto_increment primary key, money int not null)'
cursor.execute(sql)

cursor.close()
db.close()
