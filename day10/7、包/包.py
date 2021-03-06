'''
思考：如果不同的人编写的模块同名怎么办
解决：为了解决模块命名的冲突，引入了按目录来组织模块的方法，称为包
特点：引入包以后，只要顶层的包不予其他人发生冲突那么模块就不会与别人发生冲突
注意：目录只有包含一个叫做"__init__.py"的文件才被认作是一个包，主要是为了
避免一些滥俗的名字（比如叫做 string）不小心的影响搜索路径中的有效模块。
基本上目前这个文件中什么也不用写
'''
