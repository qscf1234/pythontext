import win32com
import win32com.client
import os

def readWordFileToOtherFile(path, toPath):
    mw = win32com.client.Dispatch("Word.Application")
    doc = mw.Documents.Open(path)
    # 将word的数据保存到另一个文件
    doc.SaveAs(toPath, 2)  # 2表示为txt文件

    doc.Close()
    mw.Quit()

path = os.getcwd() + '\\sunck.doc'
toPath =  os.getcwd() + '\\a.txt'
readWordFileToOtherFile(path, toPath)

