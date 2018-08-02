import re
'''
给一个字符串判断是否是手机号
'''

def checkPhone(str):
    if len(str) != 11:
        return False
    elif str[0] != '1':
        return False
    elif str[1:3] != ('39' or '31'):
        return False
    for i in str:
        if i < '0' or i > '9':
            return False
    return True

print(checkPhone("13912345678"))
print(checkPhone("139123456791"))
print(checkPhone("1391234a678"))
print(checkPhone("23912345678"))
print(checkPhone("19012345678"))
print('******************************')
def checkPhone2(str):
    pat = r'^1(39|31)\d{8}$'
    res = re.match(pat, str)
    # print(re.match(pat, str))
print(checkPhone2("13912345678"))
print(checkPhone2("139123456791"))
print(checkPhone2("1391234a678"))
print(checkPhone2("23912345678"))
print(checkPhone2("19012345678"))

'''
QQ        6到10位，全是数字
mail      suncksunck@163.com
phone     010-55348765
user      6到12位
passwd
ip
url
'''
re_QQ = re.compile(r"^[1-9]\d{5,10}$")
print(re_QQ.search("12345678901"))
re_mail = re.compile('(\A\S+)(@)(\S{1,5})(.com\Z)')
print(re_mail.findall('suncksunck@163.com'))
print(re_mail.findall('suncksunck@qq.com'))
print(re_mail.search('suncksunck@163.com'))
print(re_mail.search('suncksunck@qq.com'))
