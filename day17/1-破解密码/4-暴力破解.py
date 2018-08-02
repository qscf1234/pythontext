import time
import itertools

passwd = ("".join(x) for x in itertools.product("0123456789QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm", repeat=10))
while True:
    try:
        str1 = next(passwd)
        time.sleep(0.0000000000000000000000000000000000000000000000000000000000000001)
        print(str1)
    except StopIteration as e:
        break
