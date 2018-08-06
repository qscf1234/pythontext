import redis

class SunckRedis():
    def __init__(self, passwd, host="localhost", port=6379):
        self.__redis = redis.StrictRedis(host=host, port=port, password=passwd)

    def set(self, key, value):
        self.__redis.set(key, value)
    def get(self,key):
        if self.__redis.exists(key):
            return self.__redis.get(key)
        else:
            return ""
