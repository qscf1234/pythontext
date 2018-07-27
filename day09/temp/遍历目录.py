'''
方法一：递归遍历
'''
# import os
# path = r'D:\pythontext\day09\temp'
# def getalldir(path):
#     filelist = os.listdir(path)
#     for filename in filelist:
#         fileabspath = os.path.join(path, filename)
#         if os.path.isdir(fileabspath):
#             print('目录'+filename)
#             getalldir(fileabspath)
#         else:
#             print('文件'+filename)
#
# getalldir(path)

''''
方法二：栈模拟遍历
'''
# import os
# path = r'D:\pythontext\day09\temp'
#
# def getalldirst(path):
#     stack = []
#     stack.append(path)
#     while len(stack) !=0:
#         filepath = stack.pop()
#         filelist = os.listdir(filepath)
#         for filename in filelist:
#             fileabspath = os.path.join(filepath, filename)
#             if os.path.isdir(fileabspath):
#                 stack.append(fileabspath)
#                 print(filename)
#             else:
#                 print(filename)
#
# getalldirst(path)
'''
方法三：队列模拟遍历
'''
import collections
import os
path = r'D:\pythontext\day09\temp'
def getalldirqu(path):
    queue = collections.deque()
    queue.append(path)
    while len(queue) != 0:
        filepath = queue.popleft()
        filelist = os.listdir(filepath)
        for filename in filelist:
            fileabspath = os.path.join(filepath, filename)
            if os.path.isdir(fileabspath):
                queue.append(fileabspath)
                print('目录' + filename)
            else:
                print('文件' + filename)

getalldirqu(path)