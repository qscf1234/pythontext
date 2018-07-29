import tkinter
win = tkinter.Tk()
win.title('我')
# win.geometry('400x400+500+50')
'''
文本控件，用于显示多行文本
'''
# 创建滚动条
scroll = tkinter.Scrollbar()
text = tkinter.Text(win, width=50, height=4)
# side放到窗体的那一侧   fill填充
scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
text.pack(side=tkinter.LEFT, fill=tkinter.Y)
# 关联
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)

str = 'If there is anyone out there who still doubts that America is a place where all things are possible, who still wonders if the dream of our founders is alive in our time, who still questions the power of our democracy, tonight is your answerIf there is anyone out there who still doubts that America is a place where all things are possible, who still wonders if the dream of our founders is alive in our time, who still questions the power of our democracy, tonight is your answer'
text.insert(tkinter.INSERT, str)
win.mainloop()
