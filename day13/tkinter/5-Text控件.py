import tkinter
win = tkinter.Tk()
win.title('我')
win.geometry('400x400+500+50')
'''
文本控件，用于显示多行文本
'''
# width显示宽度  height显示的行数
text = tkinter.Text(win, width=50, height=5)
text.pack()
str = 'If there is anyone out there who still doubts that America is a place where all things are possible, who still wonders if the dream of our founders is alive in our time, who still questions the power of our democracy, tonight is your answer'
text.insert(tkinter.INSERT, str)
win.mainloop()
