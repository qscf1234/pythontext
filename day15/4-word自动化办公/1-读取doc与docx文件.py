import win32com
import win32com.client
import os

def readWoedFile(path):
    # 调用系统word功能，可以处理doc和docx两种文件
    mw = win32com.client.Dispatch("Word.Application")
    # 打开文件
    doc = mw.Documents.Open(path)
    for paragraph in doc.Paragraphs:
        line = paragraph.Range.Text
        print(line)
    # 关闭文件
    doc.Close()
    # 退出word
    mw.Quit()

path = os.getcwd() + '\\sunck.doc'
readWoedFile(path)











