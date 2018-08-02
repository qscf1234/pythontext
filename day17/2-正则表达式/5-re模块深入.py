import re

'''
字符串切割
'''
str1 = 'sunck             is a good man'
print(str1.split(' '))
print(re.split(r' +', str1))

'''
re.finditer函数
原型：finditer(pattern, string, flags=0)
参数：
patter: 匹配的正则表达式
string: 要匹配的字符串
flags:标志位，用于控制正则表达式的匹配方式
功能：与findall类似，扫描整个字符串，返回的是一个迭代器
'''
str3 = "sunck is a good man! sunck is a nice man! sunck is a handsome man"
d = re.finditer(r"(sunck)", str3)
while True:
    try:
        l = next(d)
        print(d)
    except StopIteration as e:
        break
'''
字符串的替换和修改
sub(pattern, repl, string, count=0)
subn(pattern, repl, string, count=0)
pattern:  正则表达式(规则)
repl:     指定的用来替换的字符串
string:   目标字符串
count:    最多替换次数
功能：在目标字符串中以正则表达式的规则匹配字符串，再把他们替换成指定的字符串。可以指定替换的次数,如果不指定，替换所有的匹配字符串

区别：前者返回一个被替换的字符串，后者返回一个元组，第一个元素被替换的字符串，第二个元素表示被替换的次数
'''
str5 = "sunck is a good good good man"
print(re.sub(r"(good)", "nice", str5))
print(type(re.sub(r"(good)", "nice", str5)))
print(re.subn(r"(good)", "nice", str5))
print(type(re.subn(r"(good)", "nice", str5)))


'''
分组：
概念：除了简单的判断是否匹配之外，正则表达式还有提取子串的功能。用()表示的就是提取分组
'''
str6 = "010-5324765454"
m = re.match(r"(?P<first>\d{3})-(?P<last>\d{8})", str6)
# 使用序号获取对应组的信息，group(0)一直代表的原始字符串
print(m)
print(m.group(0))
print(m.group(1))
print(m.group("first"))
print(m.group(2))
# 查看匹配的各组的情况
print(m.groups())

'''
编译：当我们使用正则表达式时，re模块会干两件事
1、编译正则表达式，如果正则表达式本身不合法，会报错
2、用编译后的正则表达式去匹配对象
compile(pattern, flags=0)
pattern:要编译的正则表达式
'''
print('*****************************')
pat = r"^1(([3578]\d)|(47))\d{8}$"
print(re.match(pat, "13600000000"))
# 编译成正则对象
re_telephon = re.compile(pat)
print(re_telephon.match("13600000000"))



# re模块调用
# re对象调用
# re.match(pattern, string, flags=0)
# re_telephon.match(string)
# re.search(pattern, string, flags=0)
# re_telephon.search(sting)
# re.findall(pattern, string, flags=0)
# re_telephon.findall(string)
# re.finditer(pattern, string, flags=0)
# re_telephon.finditer(string)
# re.split(pattern, string, maxsplit=0, flags=0)
# re_telephon.split(string, maxsplit=0)
# re.sub(pattern, repl, string, count=0, flags=0)
# re_telephon.sub(repl, string, count=0)
# re.subn(pattern, repl, string, count=0, flags=0)
# re_telephon.subn(repl, string, count=0)
#