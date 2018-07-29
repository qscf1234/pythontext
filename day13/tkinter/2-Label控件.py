import tkinter
win = tkinter.Tk()
win.title('我')
win.geometry('400x400+500+50')
'''
label1：标签控件可以显示文本
'''
# win 父窗体  text显示文本内容   bg 背景色  fg 字体颜色  font 字体               wraplength 多宽后换行 justify 对齐方式   anchor   位置  (n北  e东  s南  w西  center居中  ne   se   sw   nw)
label1 = tkinter.Label(win, text='sunck is a good man', bg='blue', fg='red',
                       font=('黑体', 30), wraplength=100, justify='left', anchor='center')
# 显示出来
label1.pack()
win.mainloop()
