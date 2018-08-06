import redis

# 连接
r = redis.StrictRedis(host="localhost", port=6379, password="sunck")

# 方法1：根据数据类型的不同，调用响应的方法
# 写
# r.set("p1", "good")
# 读
# print(r.get("p1"))

# 方法2：pipeline
# 缓冲多条命令，然后依次执行，减少服务器-客户端之间的TCP数据包
pipe = r.pipeline()
pipe.set("p2", "nice")
pipe.set("p3", "handsom")
pipe.set("p4", "cool")
pipe.execute()
