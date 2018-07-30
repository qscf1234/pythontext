import tkinter
from tkinter import ttk
import os

class TreeWindows(tkinter.Frame):
    def __init__(self, master, path, otherWin):
        frame = tkinter.Frame(master)
        frame.grid(row=2, column=0)

        self.otherWin = otherWin
        self.tree = ttk.Treeview(frame)
        self.tree.pack(side=tkinter.LEFT, fill=tkinter.Y)
        root = self.tree.insert('', 'end', text=os.path.split(path)[-1], open=True, values=(path.encode('unicode_escape')))
        self.loadTree(root, path)
        # 滚动条
        self.sy = tkinter.Scrollbar(frame)
        self.sy.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.sy.config(command=self.tree.yview)
        self.tree.config(yscrollcommand=self.sy.set)
        # 绑定事件
        self.tree.bind('<<TreeviewSelect>>', self.func1)

    def loadTree(self, parent, parentPath):
        for filePath in os.listdir(parentPath):
            absPath = os.path.join(parentPath, filePath)
            # 插入树枝
            treey = self.tree.insert(parent, 'end', text=os.path.split(absPath)[-1],values=(absPath.encode('unicode_escape')))
            if os.path.isdir(absPath):
                self.loadTree(treey, absPath)

    def func1(self, event):
        self.v = event.widget.selection()
        for sv in self.v:
            file = self.tree.item(sv)['text']
            self.otherWin.ev.set(file)
            apath = self.tree.item(sv)['values'][0]
        if os.path.isfile(apath):
            if os.path.splitext(apath)[-1] == ('.py' or '.c' or '.md'):
                try:
                    f = open(apath, encoding='utf-8')
                    message = f.read()
                except UnicodeDecodeError as e:
                    f = open(apath, encoding='gbk')
                    message = f.read()
                finally:
                    f.close()
                self.otherWin.text.delete(0.0, tkinter.END)
                self.otherWin.text.insert(tkinter.INSERT, message)

'''
    # 清除text中的所有内容
    text.delete(0.0, tkinter.END)
    text.insert(tkinter.INSERT, message)
'''