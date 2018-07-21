'''
字符串是以单引号或多引号括起来的任意文本
‘abc’
"def"
'''
# 创建字符串

str1 = 'sunck is a good man'
str3 = 'sunck is a nice man'
str5 = 'sunck is a handsome man'
'''
字符串运算
'''
# 字符串连接
str6 = 'sunk is a '
str7 = 'good man'
str8 = str6+str7
print(str8)
# 输出重复的字符串
str9 = 'good '
str10 = str9 * 3
print(str10)
# 访问字符串中的某一个字符
# 通过索引下标查找字符，索引从0开始

str11 = 'sunck is a good man'
print(str11[1])
str12 = 's沙nck is a good man'
print(str12[1], str12[2])
'''字符串不可变
截取字符串中的一部分
省略前面的从头截取到下标之前，不包括后面的那个下标的字母
省略后面的截到最后一个
'''
str13 = 'sunck is a good man'
str14 = str13[0:2]
print(str14)

print('good' in str13)
print('good1'not in str13)

# 格式化输出 占位符  转义字符 (\\)输出\
num = 10
f = 10.1234
print('num=', num)
print('num=%d\n str1=%s\n f=%.3f\n ' % (num, str1, f))
# \\ \' "" \" \t制表符
print('\'\',\" \" \t,')
# 如果字符串中有很多换行用\n卸载下一行不好阅读
print(''''
good
nice
man
''')
# 如果字符中有好多需要转义就需要加入\，为了简化
# 。python允许用r表示内部的字符串默认不转义
print(r'\\\\\\\\\t')
# eval(str) 将字符串str当成有效的表达式来求值并返回计算结果
num1 = eval('123')
print(num1, type(num1))
print(eval('-123'))
print(eval('123+1'))

# len(str) 返回字符串的长度（字符个数）
# str.lower(str)转换字符串中的大写字母为小写
str20 = 'SUNCK is a good man'
print(str20.lower())
print(str20)
# str.upper() 转换字符串中的小写字符为大写
print(str20.upper())
# swapcase() 将字符串的大写变小写，小写变大写
print(str20.swapcase())
# capitalize 首字母大写，其他小写
print(str20.capitalize())
# title() 每个单词的首字母大写
print(str20.title())
# center(width, fillchar)  fillchar 填充字符
print(str20.center(40, '*'))
'''
1
capitalize()
将字符串的第一个字符转换为大写
2	
center(width, fillchar)

返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。
3	
count(str, beg= 0,end=len(string))

返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
4	
bytes.decode(encoding="utf-8", errors="strict")

Python3 中没有 decode 方法，但我们可以使用 bytes 对象的 decode() 方法来解码给定的 bytes 对象，这个 bytes 对象可以由 str.encode() 来编码返回。
5	
encode(encoding='UTF-8',errors='strict')

以 encoding 指定的编码格式编码字符串，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'
6	
endswith(suffix, beg=0, end=len(string))
检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.
7	
expandtabs(tabsize=8)

把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8 。
8	
find(str, beg=0 end=len(string))

检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1
9	
index(str, beg=0, end=len(string))

跟find()方法一样，只不过如果str不在字符串中会报一个异常.
10	
isalnum()

如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True,否则返回 False
11	
isalpha()

如果字符串至少有一个字符并且所有字符都是字母则返回 True, 否则返回 False
12	
isdigit()

如果字符串只包含数字则返回 True 否则返回 False..
13	
islower()

如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
14	
isnumeric()

如果字符串中只包含数字字符，则返回 True，否则返回 False
15	
isspace()

如果字符串中只包含空白，则返回 True，否则返回 False.
16	
istitle()

如果字符串是标题化的(见 title())则返回 True，否则返回 False
17	
isupper()

如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
18	
join(seq)

以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
19	
len(string)

返回字符串长度
20	
ljust(width[, fillchar])

返回一个原字符串左对齐,并使用 fillchar 填充至长度 width 的新字符串，fillchar 默认为空格。
21	
lower()

转换字符串中所有大写字符为小写.
22	
lstrip()

截掉字符串左边的空格或指定字符。
23	
maketrans()

创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
24	
max(str)

返回字符串 str 中最大的字母。
25	
min(str)

返回字符串 str 中最小的字母。
26	
replace(old, new [, max])

把 将字符串中的 str1 替换成 str2,如果 max 指定，则替换不超过 max 次。
27	
rfind(str, beg=0,end=len(string))

类似于 find()函数，不过是从右边开始查找.
28	
rindex( str, beg=0, end=len(string))

类似于 index()，不过是从右边开始.
29	
rjust(width,[, fillchar])

返回一个原字符串右对齐,并使用fillchar(默认空格）填充至长度 width 的新字符串
30	
rstrip()

删除字符串字符串末尾的空格.
31	
split(str="", num=string.count(str))

num=string.count(str)) 以 str 为分隔符截取字符串，如果 num 有指定值，则仅截取 num 个子字符串
32	
splitlines([keepends])

按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
33	
startswith(str, beg=0,end=len(string))

检查字符串是否是以 obj 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查。
34	
strip([chars])

在字符串上执行 lstrip()和 rstrip()
35	
swapcase()

将字符串中大写转换为小写，小写转换为大写
36	
title()

返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())
37	
translate(table, deletechars="")

根据 str 给出的表(包含 256 个字符)转换 string 的字符, 要过滤掉的字符放到 deletechars 参数中
38	
upper()

转换字符串中的小写字母为大写
39	
zfill (width)

返回长度为 width 的字符串，原字符串右对齐，前面填充0
40	
isdecimal()

检查字符串是否只包含十进制字符，如果是返回 true，否则返回 false。
'''
print(str20.ljust(40, '$'))
'''
ord 字符串转ASCII
chr ASCII转字符串
'''

