# 一个.py文件就是一个模块

# 每一个模块都有一个__name__属性，当其值等于"__main__"时，表明该模块自身在执
# 行。否则被引入其他文件

#当前文件如果为程序的入口文件，则__name__属性的值为__main__
if __name__ == "__main__":
    print("这是sunck.py")
else:
    print(__name__)
    def sayGood():
        print("sunck is a very good man!")
    def sayNice():
        print("sunck is a nice man!")
    def sayHandsome():
        print("sunck is a handsome man!")
