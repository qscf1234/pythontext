import time
time.clock()
sum1 = 0
for i in range(100000000):
    sum1 += i
print(sum1)
print(time.clock())
