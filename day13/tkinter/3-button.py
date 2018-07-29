import tkinter
def func1():
    print('sunck is a good man')
win = tkinter.Tk()
win.title('我')
win.geometry('400x400+500+50')
button1 = tkinter.Button(win, text="按钮", command=func1, width=10, height=10)
# 显示出来
button1.pack()

button2 = tkinter.Button(win, text="结束", command=win.quit)
button2.pack()
button3 = tkinter.Button(win, text="按钮", command=lambda :print('匿名函数'))
button3.pack()
win.mainloop()
