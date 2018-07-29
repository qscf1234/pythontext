import tkinter
def func1():
    print(e.get())

win = tkinter.Tk()
win.title('我')
win.geometry('400x400+500+50')
'''
输入控件
用于显示简单的文本内容
'''
# 绑定变量
e = tkinter.Variable()
# show  密文显示   show="*"
entry = tkinter.Entry(win, textvariable=e)
entry.pack()

# e就代表输入框这个对象
# 设置值
e.set("请输入字符串")
# 取值
print(e.get())
button1 = tkinter.Button(win, text="按钮", command=func1)
button1.pack()


win.mainloop()

