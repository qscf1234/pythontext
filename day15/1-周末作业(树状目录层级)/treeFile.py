import tkinter
import os

from treeWindows import TreeWindows
from infowindows import InfoWindows

def func1():
    print(path.get())
    infoWin = InfoWindows(win)
    treeWin = TreeWindows(win, path.get(), infoWin)

win = tkinter.Tk()
win.title('树状目录')
# win.geometry('900x400+200+50')

path = tkinter.Variable()
path.set(r'D:\pythontext')
#show  密文显示   show="*"
entry = tkinter.Entry(win, textvariable=path)
entry.grid(row=0, column=0)
tkinter.Button(win, text='确定目录', command=func1).grid(row=1, column=0, sticky='nsew', pady=4)

win.mainloop()

# https://www.cnblogs.com/bambipai/p/6770447.html
