from pymongo import MongoClient

# 连接服务器
conn = MongoClient('localhost', 27017)

# 连接数据库
db = conn.mydb

# 获取集合
collection = db.student

# 添加文档
# collection.insert({"name": "abc", "age": 19, "gender": 1, "address": "北京", "isDelete": 0})
collection.insert([{"name": "abc1", "age": 19, "gender": 1, "address": "北京", "isDelete": 0}, {"name": "abc2", "age": 19, "gender": 1, "address": "北京", "isDelete": 0}])

# 断开
conn.close()
