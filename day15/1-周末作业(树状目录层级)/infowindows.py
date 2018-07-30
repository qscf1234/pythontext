import tkinter

class InfoWindows(tkinter.Frame):
    def __init__(self, master):
        frame = tkinter.Frame(master)
        frame.grid(column=1)

        self.ev = tkinter.Variable()
        self.entry = tkinter.Entry(frame, textvariable=self.ev)
        self.entry.pack()

        self.text = tkinter.Text(frame)
        self.text.pack(side=tkinter.LEFT, fill=tkinter.Y)

        # 滚动条
        self.sy1 = tkinter.Scrollbar(frame)
        self.sy1.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.sy1.config(command=self.text.yview)
        self.text.config(yscrollcommand=self.sy1.set)
