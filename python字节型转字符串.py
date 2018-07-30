a = b'\xc2\xed\xb2\xae\xc0\xd6'
d = '\u6D4B\u8BD5\u7ED3\u679C'
c = u'\u5269\u4f59\u6761\u6570\u4e0d\u8db3'
print(a)
print(d)
print(c)
a
print(a.decode('gbk'))

# bytes object
b = b"example"

# str object
s = "example"

# str to bytes
bytes(s, encoding="utf8")

# bytes to str
str(b, encoding="utf-8")

# an alternative method
# str to bytes
str.encode(s)

# bytes to str
bytes.decode(b)

