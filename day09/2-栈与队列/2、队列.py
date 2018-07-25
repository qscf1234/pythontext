'''
队列：先进先出
'''
# 创建一个队列
import collections
queue = collections.deque()
print(queue)

# 进队
queue.append('A')
print(queue)
queue.append('B')
print(queue)
queue.append('C')
print(queue)

# 出队
res = queue.popleft()
print('res= ', res, '              ', queue)
res = queue.popleft()
print('res= ', res, '              ', queue)
res = queue.popleft()
print('res= ', res, '              ', queue)
