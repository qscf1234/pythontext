'''
栈：先进后出
'''
# 模拟栈结构
stack = []

# 压栈（向栈里存数据）
stack.append('A')
print(stack)
stack.append('B')
print(stack)
stack.append('C')
print(stack)

# 弹栈
res = stack.pop()
print('res= ', res, '              ', stack)
res = stack.pop()
print('res= ', res, '              ', stack)
res = stack.pop()
print('res= ', res, '              ', stack)
