import pymysql

db = pymysql.connect("localhost", "root", "root", "kaige")
cursor = db.cursor()

sql = 'update bandcard set money=1000 where id=1'
try:
    cursor.execute(sql)
    db.commit()
except:
    # 如果提交失败，回滚到上一次数据
    db.rollback()

cursor.close()
db.close()
